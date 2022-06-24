<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {},
  data () {
    return {
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,300;0,500;0,700;1,100;1,300;1,500;1,600&display=swap');

$primary-color: #362490;
$secondary-color: #5721AB;
$third-color: #551778;
$four-color: #B211AD;
$rose: #ff35ae;
$red: #c60d48;

* {
  margin: 0;
  padding: 0;
  
  a {all: unset;}

  #app {
    font-family: 'Poppins', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .btn-0 {
    span {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      padding: 10px 0;
      color: white;
      background-color: $four-color;
      background-image: linear-gradient(60deg, $primary-color, rgba(255,255,255,0));
      border-radius: 5px;
      border: 1px solid $primary-color;
      transition: background-color 700ms;
    }
    &:hover {
      cursor: pointer;
      span {
        background-color: $primary-color;
      }
    }
  }

  .btn-1 {
    span {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      padding: 10px 0;
      color: white;
      background-color: #ff35ae;
      background-image: linear-gradient(60deg, $red, rgba(255,255,255,0));
      border-radius: 5px;
      border: 1px solid $red;
      transition: background-color 700ms;
    }
    &:hover {
      cursor: pointer;
      span {
        background-color: $red;
      }
    }
  }
}
</style>
