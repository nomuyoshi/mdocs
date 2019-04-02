<template>
  <aside class="menu">
    <p class="menu-label has-text-white has-text-weight-bold">
      <b-icon icon="thumbtack" size="is-small"></b-icon>
      ピン
    </p>
    <ul class="menu-list">
      <li class="is-size-7">
        <router-link :to="{ name: 'doc-list', query: { pin: true }}">
          ピンどめドキュメント
        </router-link>
      </li>
    </ul>
    <p class="menu-label has-text-white has-text-weight-bold">
      <b-icon icon="tags" size="is-small"></b-icon>
      タグ
    </p>
    <ul class="menu-list">
      <li v-for="tag in tags" :key="tag.id" class="is-size-7">
        <router-link :to="{ name: 'doc-list', query: { tag: tag.name }}">
          {{ tag.name }} ({{ tag.documents_count }})
        </router-link>
      </li>
    </ul>
  </aside>
</template>

<script>
import axios from 'axios';
import NotificationMixin from '@/mixins/NotificationMixin';

const SidebarMenu = {
  data() {
    return {
      tags: [],
    };
  },
  mounted() {
    axios.get('/tags/')
      .then((response) => {
        this.tags = response.data;
      })
      .catch(() => {
        this.notifyError('タグの取得に失敗しました。時間をおいて再度お試しください。');
      });
  },
  mixins: [NotificationMixin],
};

export default SidebarMenu;
</script>

<style lang="scss" scoped>
.menu {
  height: 75%;
  overflow-y: auto;

  .menu-list {
    a {
      color: white;
      &:hover {
        color: $grey-dark;
      }
    }
    .router-link-exact-active {
      @extend .is-active;
    }
  }
}
</style>
