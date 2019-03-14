<template>
  <div id="preview">
    <div v-html="compiledHtml"></div>
    <p class="has-text-grey-light" style="margin-top: 1em;" v-show="noData">
      プレビューエリア
    </p>
  </div>
</template>

<script>
const Preview = {
  props: {
    compiledHtml: String,
  },
  computed: {
    noData() {
      return this.compiledHtml.length === 0;
    },
  },
};

export default Preview;
</script>

<style lang="scss" scoped>
@import '~bulma/sass/utilities/_all.sass';
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
    margin-top: 0;
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
    margin-left: 1.5rem;
    ul {
      list-style-type: circle;
      ul {
        list-style-type: square;
      }
    }
  }
  /deep/ ol {
    margin-left: 2.5rem;
  }
}
</style>
