export default {
  methods: {
    notifySuccess(title) {
      this.$notify({
        group: 'notifications',
        type: 'success',
        title,
      });
    },
    notifyError(text) {
      this.$notify({
        group: 'notifications',
        type: 'error',
        title: 'エラー',
        text,
      });
    },
  },
};
