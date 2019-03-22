<template>
  <div id="preview" :class="previewCss">
    <div v-html="compiledHtml"></div>
    <p class="has-text-grey-light" style="margin-top: 1em;" v-show="noData">
      プレビューエリア
    </p>
  </div>
</template>

<script>
import marked from 'marked';

const Preview = {
  props: {
    markdown: {
      type: String,
      default: '',
    },
    inputting: {
      type: Boolean,
      default: false,
    },
    scrollPercents: {
      type: Number,
    },
  },
  computed: {
    compiledHtml() {
      return marked(this.markdown, { sanitize: true, breaks: true });
    },
    noData() {
      return this.markdown.length === 0;
    },
    previewCss() {
      return this.inputting ? 'preview-scroll' : '';
    },
  },
  watch: {
    scrollPercents(newValue) {
      const el = this.$el;
      const distance = (el.scrollHeight - el.clientHeight) * newValue;
      el.scrollTo(0, distance);
    },
  },
};

export default Preview;
</script>

<style lang="scss" scoped>
@import '~bulma/sass/utilities/_all.sass';
.preview-scroll {
  height: calc(100vh - 250px);
  overflow-y: auto;
}

#preview {
  /deep/h1, /deep/h2, /deep/h3, /deep/h4, /deep/h5, /deep/h6 {
    font-weight: $weight-bold;
    margin-top: 1.6rem;
    margin-bottom: 1.4rem;
  }
  /deep/ h1 {
    font-size: 2rem;
    padding-bottom: .2rem;
    border-bottom: 1px solid $border;
    margin-bottom: 2rem;
  }
  /deep/ h2 {
    font-size: 1.8rem;
    padding-bottom: .2rem;
    border-bottom: 1px solid $border;
    margin-bottom: 2rem;
  }
  /deep/ h3 { font-size: 1.6rem; }
  /deep/ h4 { font-size: 1.4rem; }
  /deep/ h5 { font-size: 1.2rem; }
  /deep/ h6 { font-size: 1.0rem; }
  /deep/ ul {
    list-style: disc inside none;
    margin-top: 1rem;
    margin-bottom: 1rem;
    margin-left: 1.5rem;
    ul {
      list-style-type: circle;
      ul {
        list-style-type: square;
      }
    }
  }
  /deep/ ol {
    margin-top: 1rem;
    margin-bottom: 1rem;
    margin-left: 2.5rem;
  }
  /deep/ blockquote {
    background-color: whitesmoke;
    font-size: 1rem;
    border-color: $border;
    border-radius: $radius;
    border-style: solid;
    border-width: 0 0 0 4px;
    color: $grey;
    padding: 1.25em 1.5em;
    margin: 1.5em 0;
  }
  /deep/ table {
    margin: 1.5rem 0;
    background-color: $white;
    color: $grey-darker;
    tr {
      td, th {
        border: 1px solid $grey-lighter;
        border-width: 1px;
        padding: .5em .75em;
        vertical-align: top;
      }
    }
    tbody {
      tr:nth-child(even) {
        background-color: $white-ter;
      }
    }
  }
  /deep/ p+p {
    margin-top: 1.5rem;
  }
  /deep/ pre {
    margin: 1.5rem 0;
  }
  /deep/ img {
    margin: 1.5rem 0;
  }
}
</style>
