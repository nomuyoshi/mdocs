/* eslint-disable */
import customMarked from 'marked';
import hljs from 'highlight.js';

const renderer = new customMarked.Renderer();
renderer.code = function(code, infostring, escaped) {
  const lang = (infostring || '').match(/\S*/)[0];
  const out = hljs.highlightAuto(code, [lang]).value;

  if (!lang) {
    return `<pre><code class="hljs">${out}</code></pre>`;
  }

  return '<pre><code class="hljs '
    + this.options.langPrefix
    + escape(lang, true)
    + '">'
    + out
    + '</code></pre>\n';
};
export default renderer;
