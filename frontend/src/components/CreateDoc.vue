<template>
  <div>
    <b-field>
      <b-input v-model="title" placeholder="タイトル"></b-input>
    </b-field>
    <hr>
    <div class="columns body-area">
      <div class="column is-half">
        <div class="editor">
          <b-field>
            <b-input type="textarea" placeholder="本文" @input="updateBody" :value="body"/>
          </b-field>
        </div>
      </div>
      <div class="column is-half">
        <preview :compiled-html="compiledHtml"/>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <button class="button primary is-pulled-right" type="button">保存</button>
      </div>
    </div>
  </div>
</template>

<script>
import marked from 'marked';
import { debounce } from 'lodash';
import Preview from './Preview.vue';

export default {
  data() {
    return {
      title: '',
      body: '',
    };
  },
  computed: {
    compiledHtml() {
      return marked(this.body, { sanitize: true, breaks: true });
    },
  },
  methods: {
    // eslint-disable-next-line func-names
    updateBody: debounce(function (value) {
      this.body = value;
    }, 300),
  },
  components: {
    Preview,
  },
};
</script>

<style lang="scss" scoped>
.body-area {
  height: calc(100vh - 200px);
}
</style>
