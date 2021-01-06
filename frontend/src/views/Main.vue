<template>
  <main class="main">
    <Aside />
    <Section/>
  </main>
</template>

<script>
import Aside from "./Aside";
import Section from "./Section";

export default {
  name: 'Main',
  components: {
    Aside, Section
  },
}
</script>

<style scoped lang="scss">
main {
  display: flex;
  min-height: calc(100vh - (20vh + 150px));
}
</style>
