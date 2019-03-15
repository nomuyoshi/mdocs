// eslint-disable-next-line import/prefer-default-export
export const scroll = {
  name: 'scroll',
  inserted(el, binding) {
    const func = (event) => {
      if (binding.value(event, el)) {
        el.removeEventListener('scroll', func);
      }
    };
    el.addEventListener('scroll', func);
  },
};
