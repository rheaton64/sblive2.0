<template>
  <v-container fill-height >
    <v-row align="center">
            <Start v-if="isInit" v-on:init-base="initBase()" v-on:init-controller="initController()"/>
            <Base v-if="isBase" />
            <Controller v-if="isController" />
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import Start from '@/components/Start'
import Base from '@/components/Base'
import Controller from "@/components/Controller"

export default {
  name: 'Home',
  components: {
    Start,
    Base,
    Controller
  },
  data() {
    return {
      isInit: true,
      isBase: false,
      isController: false
    }
  },
  methods: {
    initBase: function () {
      this.isInit = false
      this.isBase = true
    },
    initController: function () {
      this.isInit = false
      this.isController = true
      console.log('Controller?')
    }
  }
}
</script>
