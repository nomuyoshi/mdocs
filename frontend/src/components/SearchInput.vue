<template>
  <b-field>
    <b-input placeholder="タイトル検索"
      type="search"
      icon="search"
      @keyup.native.enter="search"
     >
    </b-input>
  </b-field>
</template>

<script>
const SearchInput = {
  methods: {
    search(event) {
      const title = event.target.value.trim();
      if (!title) { return; }

      this.$router.push({ name: 'doc-list', query: { title } });
    },
  },
};
export default SearchInput;
</script>
