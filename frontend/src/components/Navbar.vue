<template>
  <nav class="navbar is-fixed-top is-dark" role="navigation" aria-label="main navigation">
    <div class="navbar-brand" :style="{ width: brandWidth + 'px'}">
      <a class="navbar-item" href="/" style="width: 100%;">
        <h1 class="has-text-white has-text-weight-bold is-size-3">mDoc</h1>
      </a>
    </div>
    <div id="navbar-menu" class="navbar-menu">
      <div class="navbar-start">
        <div class="navbar-item">
          <search-input />
        </div>
      </div>
      <div class="navbar-end">
        <a href="https://twitter.com/mDocSupportTeam" target="_blank" class="navbar-item">
          お知らせ
        </a>
        <router-link class="navbar-item" to="/contact">
          <b-icon icon="envelope" size="is-small"></b-icon>
          <span>お問い合わせ</span>
        </router-link>
        <div class="navbar-item has-dropdown is-hoverable">
          <span class="navbar-link">
            メニュー
          </span>
          <div class="navbar-dropdown is-boxed">
            <a href="/logout/" class="navbar-item">ログアウト</a>
            <hr class="navbar-divider">
            <a class="navbar-item" @click="onClickDeleteUser">退会</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
import axios from 'axios';
import SearchInput from './SearchInput.vue';
import NotificationMixin from '@/mixins/NotificationMixin';

const Navbar = {
  props: {
    brandWidth: {
      type: String,
      required: true,
    },
  },
  components: {
    SearchInput,
  },
  methods: {
    onClickDeleteUser(e) {
      e.preventDefault();
      // eslint-disable-next-line no-alert
      if (window.confirm('全データが削除され、二度と元に戻せません。よろしいですか？')) {
        axios.delete('/user/delete/')
          .then(() => {
            window.location.href = '/login';
          })
          .catch(() => {
            this.notifyError('退会できませんでした。時間をおいて再度お試しください。');
          });
      }
    },
  },
  mixins: [NotificationMixin],
};

export default Navbar;
</script>

<style lang="scss" scoped>
.navbar {
  border-bottom: 1px solid #7A7A7A;
}
</style>
