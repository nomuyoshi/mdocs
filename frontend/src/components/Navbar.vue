<template>
  <nav class="navbar is-fixed-top is-primary" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <h1 class="has-text-white is-size-3">mDoc</h1>
        <!--            <img src="{% static 'images/logo.png' %}" alt="mDocロゴ" /> -->
      </a>
      <a role="button" class="navbar-burger burger" data-target="navbar-menu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div id="navbar-menu" class="navbar-menu">
      <div class="navbar-start">
        <div class="navbar-item">
          <search-input />
        </div>
      </div>
      <div class="navbar-end">
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

const Navbar = {
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
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
};

export default Navbar;
</script>
