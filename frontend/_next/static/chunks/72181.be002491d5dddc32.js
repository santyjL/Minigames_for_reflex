(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[72181,53318,70156,93279],{72181:function(e,s,n){"use strict";var t=n(64836);Object.defineProperty(s,"__esModule",{value:!0}),s.default=void 0;var r=t(n(32268));s.default=r.default},61958:function(e){"use strict";function s(e){!function(e){function s(e,s){return e.replace(/<<(\d+)>>/g,function(e,n){return"(?:"+s[+n]+")"})}function n(e,n,t){return RegExp(s(e,n),t||"")}function t(e,s){for(var n=0;n<s;n++)e=e.replace(/<<self>>/g,function(){return"(?:"+e+")"});return e.replace(/<<self>>/g,"[^\\s\\S]")}var r="bool byte char decimal double dynamic float int long object sbyte short string uint ulong ushort var void",a="class enum interface record struct",i="add alias and ascending async await by descending from(?=\\s*(?:\\w|$)) get global group into init(?=\\s*;) join let nameof not notnull on or orderby partial remove select set unmanaged value when where with(?=\\s*{)",o="abstract as base break case catch checked const continue default delegate do else event explicit extern finally fixed for foreach goto if implicit in internal is lock namespace new null operator out override params private protected public readonly ref return sealed sizeof stackalloc static switch this throw try typeof unchecked unsafe using virtual volatile while yield";function u(e){return"\\b(?:"+e.trim().replace(/ /g,"|")+")\\b"}var c=u(a),l=RegExp(u(r+" "+a+" "+i+" "+o)),d=u(a+" "+i+" "+o),p=u(r+" "+a+" "+o),g=t(/<(?:[^<>;=+\-*/%&|^]|<<self>>)*>/.source,2),b=t(/\((?:[^()]|<<self>>)*\)/.source,2),f=/@?\b[A-Za-z_]\w*\b/.source,h=s(/<<0>>(?:\s*<<1>>)?/.source,[f,g]),m=s(/(?!<<0>>)<<1>>(?:\s*\.\s*<<1>>)*/.source,[d,h]),k=/\[\s*(?:,\s*)*\]/.source,y=s(/<<0>>(?:\s*(?:\?\s*)?<<1>>)*(?:\s*\?)?/.source,[m,k]),w=s(/[^,()<>[\];=+\-*/%&|^]|<<0>>|<<1>>|<<2>>/.source,[g,b,k]),v=s(/\(<<0>>+(?:,<<0>>+)+\)/.source,[w]),x=s(/(?:<<0>>|<<1>>)(?:\s*(?:\?\s*)?<<2>>)*(?:\s*\?)?/.source,[v,m,k]),_={keyword:l,punctuation:/[<>()?,.:[\]]/},$=/'(?:[^\r\n'\\]|\\.|\\[Uux][\da-fA-F]{1,8})'/.source,E=/"(?:\\.|[^\\"\r\n])*"/.source,S=/@"(?:""|\\[\s\S]|[^\\"])*"(?!")/.source;e.languages.csharp=e.languages.extend("clike",{string:[{pattern:n(/(^|[^$\\])<<0>>/.source,[S]),lookbehind:!0,greedy:!0},{pattern:n(/(^|[^@$\\])<<0>>/.source,[E]),lookbehind:!0,greedy:!0}],"class-name":[{pattern:n(/(\busing\s+static\s+)<<0>>(?=\s*;)/.source,[m]),lookbehind:!0,inside:_},{pattern:n(/(\busing\s+<<0>>\s*=\s*)<<1>>(?=\s*;)/.source,[f,x]),lookbehind:!0,inside:_},{pattern:n(/(\busing\s+)<<0>>(?=\s*=)/.source,[f]),lookbehind:!0},{pattern:n(/(\b<<0>>\s+)<<1>>/.source,[c,h]),lookbehind:!0,inside:_},{pattern:n(/(\bcatch\s*\(\s*)<<0>>/.source,[m]),lookbehind:!0,inside:_},{pattern:n(/(\bwhere\s+)<<0>>/.source,[f]),lookbehind:!0},{pattern:n(/(\b(?:is(?:\s+not)?|as)\s+)<<0>>/.source,[y]),lookbehind:!0,inside:_},{pattern:n(/\b<<0>>(?=\s+(?!<<1>>|with\s*\{)<<2>>(?:\s*[=,;:{)\]]|\s+(?:in|when)\b))/.source,[x,p,f]),inside:_}],keyword:l,number:/(?:\b0(?:x[\da-f_]*[\da-f]|b[01_]*[01])|(?:\B\.\d+(?:_+\d+)*|\b\d+(?:_+\d+)*(?:\.\d+(?:_+\d+)*)?)(?:e[-+]?\d+(?:_+\d+)*)?)(?:[dflmu]|lu|ul)?\b/i,operator:/>>=?|<<=?|[-=]>|([-+&|])\1|~|\?\?=?|[-+*/%&|^!=<>]=?/,punctuation:/\?\.?|::|[{}[\];(),.:]/}),e.languages.insertBefore("csharp","number",{range:{pattern:/\.\./,alias:"operator"}}),e.languages.insertBefore("csharp","punctuation",{"named-parameter":{pattern:n(/([(,]\s*)<<0>>(?=\s*:)/.source,[f]),lookbehind:!0,alias:"punctuation"}}),e.languages.insertBefore("csharp","class-name",{namespace:{pattern:n(/(\b(?:namespace|using)\s+)<<0>>(?:\s*\.\s*<<0>>)*(?=\s*[;{])/.source,[f]),lookbehind:!0,inside:{punctuation:/\./}},"type-expression":{pattern:n(/(\b(?:default|sizeof|typeof)\s*\(\s*(?!\s))(?:[^()\s]|\s(?!\s)|<<0>>)*(?=\s*\))/.source,[b]),lookbehind:!0,alias:"class-name",inside:_},"return-type":{pattern:n(/<<0>>(?=\s+(?:<<1>>\s*(?:=>|[({]|\.\s*this\s*\[)|this\s*\[))/.source,[x,m]),inside:_,alias:"class-name"},"constructor-invocation":{pattern:n(/(\bnew\s+)<<0>>(?=\s*[[({])/.source,[x]),lookbehind:!0,inside:_,alias:"class-name"},"generic-method":{pattern:n(/<<0>>\s*<<1>>(?=\s*\()/.source,[f,g]),inside:{function:n(/^<<0>>/.source,[f]),generic:{pattern:RegExp(g),alias:"class-name",inside:_}}},"type-list":{pattern:n(/\b((?:<<0>>\s+<<1>>|record\s+<<1>>\s*<<5>>|where\s+<<2>>)\s*:\s*)(?:<<3>>|<<4>>|<<1>>\s*<<5>>|<<6>>)(?:\s*,\s*(?:<<3>>|<<4>>|<<6>>))*(?=\s*(?:where|[{;]|=>|$))/.source,[c,h,f,x,l.source,b,/\bnew\s*\(\s*\)/.source]),lookbehind:!0,inside:{"record-arguments":{pattern:n(/(^(?!new\s*\()<<0>>\s*)<<1>>/.source,[h,b]),lookbehind:!0,greedy:!0,inside:e.languages.csharp},keyword:l,"class-name":{pattern:RegExp(x),greedy:!0,inside:_},punctuation:/[,()]/}},preprocessor:{pattern:/(^[\t ]*)#.*/m,lookbehind:!0,alias:"property",inside:{directive:{pattern:/(#)\b(?:define|elif|else|endif|endregion|error|if|line|nullable|pragma|region|undef|warning)\b/,lookbehind:!0,alias:"keyword"}}}});var R=E+"|"+$,B=s(/\/(?![*/])|\/\/[^\r\n]*[\r\n]|\/\*(?:[^*]|\*(?!\/))*\*\/|<<0>>/.source,[R]),N=t(s(/[^"'/()]|<<0>>|\(<<self>>*\)/.source,[B]),2),j=/\b(?:assembly|event|field|method|module|param|property|return|type)\b/.source,z=s(/<<0>>(?:\s*\(<<1>>*\))?/.source,[m,N]);e.languages.insertBefore("csharp","class-name",{attribute:{pattern:n(/((?:^|[^\s\w>)?])\s*\[\s*)(?:<<0>>\s*:\s*)?<<1>>(?:\s*,\s*<<1>>)*(?=\s*\])/.source,[j,z]),lookbehind:!0,greedy:!0,inside:{target:{pattern:n(/^<<0>>(?=\s*:)/.source,[j]),alias:"keyword"},"attribute-arguments":{pattern:n(/\(<<0>>*\)/.source,[N]),inside:e.languages.csharp},"class-name":{pattern:RegExp(m),inside:{punctuation:/\./}},punctuation:/[:,]/}}});var C=/:[^}\r\n]+/.source,M=t(s(/[^"'/()]|<<0>>|\(<<self>>*\)/.source,[B]),2),T=s(/\{(?!\{)(?:(?![}:])<<0>>)*<<1>>?\}/.source,[M,C]),A=t(s(/[^"'/()]|\/(?!\*)|\/\*(?:[^*]|\*(?!\/))*\*\/|<<0>>|\(<<self>>*\)/.source,[R]),2),O=s(/\{(?!\{)(?:(?![}:])<<0>>)*<<1>>?\}/.source,[A,C]);function P(s,t){return{interpolation:{pattern:n(/((?:^|[^{])(?:\{\{)*)<<0>>/.source,[s]),lookbehind:!0,inside:{"format-string":{pattern:n(/(^\{(?:(?![}:])<<0>>)*)<<1>>(?=\}$)/.source,[t,C]),lookbehind:!0,inside:{punctuation:/^:/}},punctuation:/^\{|\}$/,expression:{pattern:/[\s\S]+/,alias:"language-csharp",inside:e.languages.csharp}}},string:/[\s\S]+/}}e.languages.insertBefore("csharp","string",{"interpolation-string":[{pattern:n(/(^|[^\\])(?:\$@|@\$)"(?:""|\\[\s\S]|\{\{|<<0>>|[^\\{"])*"/.source,[T]),lookbehind:!0,greedy:!0,inside:P(T,M)},{pattern:n(/(^|[^@\\])\$"(?:\\.|\{\{|<<0>>|[^\\"{])*"/.source,[O]),lookbehind:!0,greedy:!0,inside:P(O,A)}],char:{pattern:RegExp($),greedy:!0}}),e.languages.dotnet=e.languages.cs=e.languages.csharp}(e)}e.exports=s,s.displayName="csharp",s.aliases=["dotnet","cs"]},32268:function(e,s,n){"use strict";var t=n(2329),r=n(61958);function a(e){e.register(t),e.register(r),e.languages.t4=e.languages["t4-cs"]=e.languages["t4-templating"].createT4("csharp")}e.exports=a,a.displayName="t4Cs",a.aliases=[]},2329:function(e){"use strict";function s(e){!function(e){function s(e,s,n){return{pattern:RegExp("<#"+e+"[\\s\\S]*?#>"),alias:"block",inside:{delimiter:{pattern:RegExp("^<#"+e+"|#>$"),alias:"important"},content:{pattern:/[\s\S]+/,inside:s,alias:n}}}}e.languages["t4-templating"]=Object.defineProperty({},"createT4",{value:function(n){var t=e.languages[n],r="language-"+n;return{block:{pattern:/<#[\s\S]+?#>/,inside:{directive:s("@",{"attr-value":{pattern:/=(?:("|')(?:\\[\s\S]|(?!\1)[^\\])*\1|[^\s'">=]+)/,inside:{punctuation:/^=|^["']|["']$/}},keyword:/\b\w+(?=\s)/,"attr-name":/\b\w+/}),expression:s("=",t,r),"class-feature":s("\\+",t,r),standard:s("",t,r)}}}}})}(e)}e.exports=s,s.displayName="t4Templating",s.aliases=[]},64836:function(e){e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports}}]);