<template>
  <div class="columns">
    <div class="column">
      <doc-detail/>
    </div>
  </div>
</template>

<script>
import DocDetail from '@/components/DocDetail.vue';

const DocDetailView = {
  components: {
    DocDetail,
  },
};

export default DocDetailView;
</script>
