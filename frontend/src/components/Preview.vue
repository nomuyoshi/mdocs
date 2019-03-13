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
@import '~bulma/sass/utilities/initial-variables.sass';
#preview {
  /deep/ h1 { font-size: $size-2; }
  /deep/ h2 { font-size: $size-3; }
  /deep/ h3 { font-size: $size-4; }
  /deep/ h4 { font-size: $size-5; }
  /deep/ h5 { font-size: $size-6; }
  /deep/ h6 { font-size: $size-6; }
  /deep/ ul {
    list-style: disc inside none;
    margin-left: 20px;
  }
}
</style>
