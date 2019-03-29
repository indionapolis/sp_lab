import {mount, shallowMount} from '@vue/test-utils'
import HelloWorld from '@/components/HelloWorld'
import Counter from '@/components/Counter'

describe('HelloWorld.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message';
    const wrapper = shallowMount(HelloWorld, {
      propsData: { msg }
    });

    expect(wrapper.text()).toMatch(msg)
  })
});

describe('Counter.vue', () => {
  const wrapper = mount(Counter);
  // wrapper.vm - vue instance, with all consts and vars

  it('two button click incrementW the count', () => {
    expect(wrapper.vm.count).toBe(0);

    const button = wrapper.find('button');

    button.trigger('click');
    button.trigger('click');

    expect(wrapper.vm.count).toBe(1)
  })
})
