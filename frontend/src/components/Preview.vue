<template>
  <div id="preview" v-html="compiledHtml"></div>
</template>

<script>
export default {
  props: {
    compiledHtml: String,
  },
};
</script>

<style lang="scss" scoped>
@import '~bulma/sass/utilities/initial-variables.sass';
#preview {
  /deep/ h1 { font-size: $size-1; }
  /deep/ h2 { font-size: $size-2; }
  /deep/ h3 { font-size: $size-3; }
  /deep/ h4 { font-size: $size-4; }
  /deep/ h5 { font-size: $size-5; }
  /deep/ h6 { font-size: $size-6; }
  /deep/ ul {
    list-style: disc inside none;
    margin-left: 20px;
  }
}
</style>
