#!/usr/bin/env python3
"""Build the evolving football guide using only Python's standard library."""
import html
import json
import posixpath
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENT = ROOT / 'events/20261021-fctokyo-kashiwa'
GITHUB = 'https://github.com/SideBySite/guide/blob/main/events/20261021-fctokyo-kashiwa/'

def front(text):
    meta = {}
    if text.startswith('---\n'):
        header, text = text[4:].split('\n---', 1)
        key = ''
        for line in header.splitlines():
            if re.match(r'^\w[\w_]*:', line):
                key, val = line.split(':', 1)
                meta[key] = val.strip().strip('\"\'')
            elif line.strip().startswith('- ') and key:
                meta[key] = (meta.get(key, '') + '\n' + line.strip()[2:]).strip()
    return meta, text.strip()

def main():
    candidates = list(EVENT.glob('content/**/*.md'))
    candidates += list(EVENT.glob('foundation-v2/drafts/*/*.md'))
    candidates += [EVENT / 'foundation-v2/facts/match.md']
    candidates += list(EVENT.glob('teams/*/people/*.md'))
    candidates += list(EVENT.glob('teams/*/lineup.md'))
    candidates = sorted(set(p for p in candidates if p.exists() and p.name != 'maker.md' and str(p.relative_to(EVENT)) != 'content/local/index.md'))
    ids = {str(p.relative_to(EVENT)): 'read-' + str(p.relative_to(EVENT)).replace('/', '--').removesuffix('.md') for p in candidates}

    def link(url, source):
        if url.startswith(('https://', 'http://', '#', 'mailto:')):
            return url
        if ':' in url.split('/')[0]:
            return '#'
        path = posixpath.normpath(posixpath.join(posixpath.dirname(source), url.split('#')[0]))
        return '#' + ids[path] if path in ids else GITHUB + path

    def inline(text, source):
        text = html.escape(text)
        tokens = []
        def keep(value):
            tokens.append(value)
            return '\x00' + str(len(tokens)-1) + '\x00'
        text = re.sub(r'\[([^\]]+)\]\(([^\s]+)\)', lambda m: keep('<a href="' + html.escape(link(html.unescape(m[2]), source), quote=True) + '">' + m[1] + '</a>'), text)
        text = re.sub(r'`([^`]+)`', lambda m: keep('<code>'+m[1]+'</code>'), text)
        text = re.sub(r'(?<!["=])(https?://[^\s<>]+)', lambda m: keep('<a href="'+m[1]+'">出典を開く ↗</a>'), text)
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'==(.+?)==', r'<mark>\1</mark>', text)
        text = re.sub(r'\x00(\d+)\x00', lambda m: tokens[int(m[1])], text)
        return text

    def markdown(body, source):
        out, para, lines = [], [], body.splitlines()
        def flush():
            if para:
                out.append('<p>'+inline(' '.join(para), source)+'</p>'); para.clear()
        i = 0
        while i < len(lines):
            s = lines[i].strip()
            if s.startswith('```'):
                flush(); code=[]; i+=1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code.append(lines[i]); i+=1
                if not source.endswith('lineup.md'):
                    out.append('<pre>'+html.escape('\n'.join(code))+'</pre>')
            elif s.startswith('|'):
                flush(); rows=[]
                while i < len(lines) and lines[i].strip().startswith('|'):
                    row=lines[i].strip().strip('|').split('|')
                    if not all(re.fullmatch(r'\s*:?-+:?\s*', c) for c in row): rows.append(row)
                    i+=1
                out.append('<div class="table-scroll"><table>')
                for n,row in enumerate(rows):
                    tag='th' if n==0 else 'td'
                    out.append('<tr>'+''.join('<'+tag+'>'+inline(c.strip(),source)+'</'+tag+'>' for c in row)+'</tr>')
                out.append('</table></div>'); continue
            elif not s:
                flush()
            elif re.match(r'^#{1,6} ',s):
                flush(); h=min(4,len(s.split()[0])+1)
                out.append(f'<h{h}>'+inline(s.lstrip('# '),source)+f'</h{h}>')
            elif s.startswith('>'):
                flush();out.append('<blockquote>'+inline(s.lstrip('> '),source)+'</blockquote>')
            elif re.match(r'^[-*] ',s) or re.match(r'^\d+\. ',s):
                flush(); out.append('<p class="list-item">• '+inline(re.sub(r'^(?:[-*]|\d+\.) ', '', s), source)+'</p>')
            elif re.fullmatch(r'[-*_]{3,}',s):
                flush();out.append('<hr>')
            else: para.append(s)
            i+=1
        flush();return '\n'.join(out)

    groups = {'はじめの5分': [], '大会と順位': [], '基本ルール': [], '判定と交代': [], '会場と行き帰り': [], '戦略と観察': [], 'FC東京': [], '柏レイソル': [], '柏・日立台': []}
    articles=[]
    for p in candidates:
        source=str(p.relative_to(EVENT)); meta,body=front(p.read_text())
        heading=re.search(r'^#{1,2} (.+)',body,re.M)
        title=meta.get('title') or meta.get('question') or (heading[1] if heading else p.stem)
        title=re.sub(r'^(?:Q\d+|\d+-\d+(?:-[a-z])?)\s+', '', title)
        if 'teams/fctokyo' in source: group='FC東京'
        elif 'teams/kashiwa' in source: group='柏レイソル'
        elif '/local/' in source: group='柏・日立台'
        elif '01R-B' in source: group='大会と順位'
        elif '01R-C' in source: group='基本ルール'
        elif '01R-D' in source: group='判定と交代'
        elif '01R-E' in source: group='会場と行き帰り'
        elif 'foundation-v2/facts' in source: group='はじめの5分'
        else:
            category=source.split('/')[1]
            group={'1':'基本ルール','2':'判定と交代','3':'大会と順位','4':'戦略と観察','5':'戦略と観察','6':'戦略と観察','7':'会場と行き帰り'}.get(category,'戦略と観察')
        aid=ids[source]
        sources=meta.get('sources','').splitlines()
        footer='<div class="sources"><a href="'+GITHUB+source+'">原稿と出典 ↗</a>'
        checked=meta.get('checked_at') or meta.get('checked_on_jst')
        if checked: footer+=' · 原稿確認 '+html.escape(checked)
        for s in sources:
            if s.startswith('https://'):footer+='<br><a href="'+html.escape(s,quote=True)+'">'+html.escape(s)+'</a>'
        footer+='</div>'
        articles.append({'id':aid,'title':title,'group':group,'text':re.sub(r'[*#=|`]', '', body),'html':markdown(body,source)+footer,'source':source})
        groups[group].append({'id':aid,'title':title})
    lineups=json.loads((EVENT/'teams/lineups-display.json').read_text())
    for team in lineups['teams']:
        starting=team['starting']
        numbers=[p['number'] for p in starting]
        placed=[n for row in team['formation_rows'] for n in row]
        if len(starting)!=11 or len(set(numbers))!=11 or sorted(numbers)!=sorted(placed):
            raise ValueError('先発一覧と配置図の11人が一致しない: '+team['key'])
        for person in starting:
            path=f"teams/{team['key']}/people/{person['slug']}.md"
            if path not in ids:
                raise ValueError('選手カードの保存先を確認できない: '+path)
    payload={'articles':articles,'groups':groups,'lineups':lineups,'updated':datetime.now(timezone(timedelta(hours=9))).strftime('%Y年%m月%d日 %H:%M（日本時間）')}
    template=(ROOT/'scripts/football_template.html').read_text()
    result=template.replace('/*__DATA__*/null',json.dumps(payload,ensure_ascii=False).replace('</','<\\/'))
    target=EVENT/'site/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(result)
    print(json.dumps({'articles':len(articles),'groups':{k:len(v) for k,v in groups.items()},'output':str(target)},ensure_ascii=False))

if __name__=='__main__':main()

