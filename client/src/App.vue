<template>
  <v-app>
    <div>
      <!-- Start of Navigation -->
        <!-- Start of app toolbar -->
        <v-app-bar app>
          <v-toolbar-title class="headline text-uppercase"
            >SpikeBall Live</v-toolbar-title
          >
          <v-spacer/>
          <ConnectHandler />
          <v-btn color='primary'>Test</v-btn>
        </v-app-bar>
        <!-- End of app toolbar -->
      <!-- End of Navigation -->

      <v-content align="center">
        <!-- Display view pages here based on route -->
        <Home />
      </v-content>
    </div>
  </v-app>
</template>

<script>
  import ConnectHandler from '@/components/ConnectHandler'
  import Home from '@/components/Home'

  export default {
    name: "App",
    components: {
      Home,
      ConnectHandler
    },
    data() {
      return {
        drawer: false // Hide mobile side menu by default
      };
    }
  };
</script>