<template>
  <div class="level">
    <div class="level-left">
      <b-taglist class="level-item">
        <b-tag v-for="tag in doc.tags" :key="tag.id" rounded>
          {{ tag.name }}
        </b-tag>
      </b-taglist>
    </div>
    <div class="level-right">
      <b-taglist class="level-item">
        <b-tag rounded>作成日: {{ doc.created_at | datetimeFormat }}</b-tag>
        <b-tag rounded>更新日: {{ doc.updated_at | datetimeFormat }}</b-tag>
      </b-taglist>
    </div>
  </div>
</template>

<script>
const DocTags = {
  props: {
    doc: {
      type: Object,
      required: true,
    },
  },
};

export default DocTags;
</script>

<style lang="scss" scoped>
.level {
  margin-top: .5rem;
}
</style>
