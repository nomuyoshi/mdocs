<template>
  <div class="pin-link is-size-7">
    <p class="has-text-white has-text-weight-bold">
      <b-icon icon="thumbtack" size="is-small"></b-icon>
      ピン
    </p>
    <router-link class="has-text-white" :to="{ name: 'doc-list', query: { pin: true }}">
      ピンどめドキュメント
    </router-link>
  </div>
</template>

<style lang="scss" scoped>
.pin-link {
  height: 10%;
  a {
    padding: .5rem;
  }
}
</style>
