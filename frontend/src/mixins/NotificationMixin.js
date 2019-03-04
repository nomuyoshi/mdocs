export default {
  methods: {
    notifySuccess(title) {
      this.$notify({
        group: 'notifications',
        type: 'success',
        title,
      });
    },
    notifyError(text = '時間をおいて再度お試しください') {
      this.$notify({
        group: 'notifications',
        type: 'error',
        title: 'エラー',
        text,
      });
    },
  },
};
