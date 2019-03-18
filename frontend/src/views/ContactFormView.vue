<template>
  <div class="section">
    <div class="columns">
      <div class="column is-three-fifths is-offset-one-fifth">
        <h2 class="title is-3">お問い合わせ</h2>
        <div class="notification">
          <a href="https://twitter.com/mDocSupportTeam" target="_blank">Twitter</a>でもお問い合わせを受け付けています。<br>
          ログインに使用しているソーシャルアカウントに登録されている<br>
          メールアドレスに返信させていただく場合がございます。
        </div>
        <b-field>
          <b-input maxlength="200" type="textarea" v-model="text"></b-input>
        </b-field>
        <button class="button is-fullwidth" :disabled="disabled" @click="onSubmit">送信</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NotificationMixin from '@/mixins/NotificationMixin';

const ContactForm = {
  data() {
    return { text: '' };
  },
  computed: {
    disabled() {
      return this.text.length === 0;
    },
  },
  methods: {
    onSubmit() {
      if (this.disabled) { return; }

      // eslint-disable-next-line no-alert
      if (window.confirm('送信してよろしいですか？')) {
        axios.post('/contact/', {
          text: this.text,
        })
          .then(() => {
            this.text = '';
            this.notifySuccess('お問い合わせありがとうございました。');
          })
          .catch(() => {
            this.notifyError('入力内容を確認してください');
          });
      }
    },
  },
  mixins: [NotificationMixin],
};

export default ContactForm;
</script>
