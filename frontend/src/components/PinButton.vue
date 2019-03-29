<template>
  <button type="button" class="button is-white" @click="togglePin">
    <b-icon icon="thumbtack" :class="iconCssClass"></b-icon>
  </button>
</template>

<script>
import axios from 'axios';
import NotificationMixin from '../mixins/NotificationMixin';

const PinButton = {
  data() {
    return { isPinned: this.doc.pin };
  },
  props: {
    doc: {
      type: Object,
      required: true,
    },
  },
  computed: {
    iconCssClass() {
      return this.isPinned ? 'has-text-primary' : 'has-text-grey-light';
    },
  },
  watch: {
    doc(newDoc) {
      this.isPinned = newDoc.pin;
    },
  },
  methods: {
    togglePin() {
      const newPin = !this.isPinned;
      axios.patch(`/docs/${this.doc.id}/`, {
        pin: newPin,
      }).then((response) => {
        this.isPinned = response.data.pin;
        const message = this.isPinned ? 'ピン!!' : 'ピン解除!!';
        this.notifySuccess(message);
      }).catch(() => {
        this.notifyError();
      });
    },
  },
  mixins: [NotificationMixin],
};

export default PinButton;
</script>
