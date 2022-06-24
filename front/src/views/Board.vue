<template>
      <div>
        <div class="container-nav">
          <div>
            <img :src="require('@/assets/screenifttt.png')" :alt="'logo ifttt'" />
          </div>
          <div class="container-button-nav">
            <a @click="profil()" class="profil"><img src="https://img.icons8.com/ios-glyphs/60/ffffff/user-male.png"/></a>
            <a @click="logout()" class="btn-3">
              <span>Log out</span>
            </a>
          </div>
        </div>
        <div class="container-body">
          <h1>Config Service</h1>
          <div class="container-configured">
            <Facebook v-if="!configured.facebook" @update-service="updateService()" />
            <Intra v-if="!configured.intra" @update-service="updateService()" />
            <Twitch v-if="!configured.twitch" @update-service="updateService()" />
            <Twitter v-if="!configured.twitter" @update-service="updateService()" />
            <News v-if="!configured.news" @update-service="updateService()" />
            <Netflix v-if="!configured.netflix" @update-service="updateService()" />
            <Amazon v-if="!configured.amazon" @update-service="updateService()" />
            <Film v-if="!configured.film" @update-service="updateService()" />

          </div>
          <h1>Already configured</h1>
          <div class="container-configured">
            <Fbconfigured v-show="configured.facebook" @update-service="updateService()" />
            <Intraconfigured v-show="configured.intra" @update-service="updateService()" />
            <Amconfigured v-show="configured.amazon" @update-service="updateService()" />
            <Neconfigured v-show="configured.netflix" @update-service="updateService()" />
            <Newconfigured v-show="configured.news" @update-service="updateService()" />
            <Ficonfigured v-show="configured.film" @update-service="updateService()" />
            <Twconfigured v-show="configured.twitch" @update-service="updateService()" />
            <Twiconfigured v-show="configured.twitter" @update-service="updateService()" />
          </div>
        </div>
      </div>
</template>

<script>
import axiosGet from '@/assets/script/api.js' 

import Facebook from '@/components/config/Facebook.vue'
import Intra from '@/components/config/Intra.vue'
import Twitch from '@/components/config/Twitch.vue'
import Twitter from '@/components/config/Twitter.vue'
import News from '@/components/config/News.vue'
import Netflix from '@/components/config/Netflix.vue'
import Amazon from '@/components/config/Amazon.vue'
import Film from '@/components/config/Film.vue'

import Fbconfigured from '@/components/service/Facebook.vue'
import Intraconfigured from '@/components/service/Intra.vue'
import Amconfigured from '@/components/service/Amazon.vue'
import Ficonfigured from '@/components/service/Film.vue'
import Neconfigured from '@/components/service/Netflix.vue'
import Newconfigured from '@/components/service/News.vue'
import Twconfigured from '@/components/service/Twitch.vue'
import Twiconfigured from '@/components/service/Twitter.vue'

export default {
  name: 'Board',
  components: {
    Facebook,
    Intra,
    Twitch,
    Twitter,
    News,
    Netflix,
    Amazon,
    Film,

    Fbconfigured,
    Intraconfigured,
    Amconfigured,
    Ficonfigured,
    Neconfigured,
    Newconfigured,
    Twconfigured,
    Twiconfigured,
  },
  data () {
    return {
      configured: {},
    }
  },
  methods: {
    profil () { console.log('profil') },
    async logout () {
        await axiosGet.post('/logout/', {})
        .then((response) => {
          console.log(response)
          localStorage.removeItem('token')
          this.$router.push('/login')
        }).catch((error) => {
          console.log(error)
        })
    },
    async updateService () {
            await axiosGet.get('/services/', {})
            .then((response) => {
                this.configured = response.data.data
                console.log(response)
            }).catch((error) => {
                console.log(error)
            })
    },
  },
  mounted () {
    this.updateService()
  },
}
</script>

<style scoped lang="scss">
$primary-color: #362490;
$secondary-color: #5721AB;
$third-color: #551778;
$four-color: #B211AD;
$rose: #ff35ae;
$red: #c60d48;
$blue: #2aadd9;

  .container-nav {
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-wrap: wrap;
    min-height: 80px;
    background-color: $four-color;
    box-shadow: 0px 3px 16px -2px rgba(178,17,173,0.75);
    -webkit-box-shadow: 0px 3px 16px -2px rgba(178,17,173,0.75);
    -moz-box-shadow: 0px 3px 16px -2px rgba(178,17,173,0.75);


    .container-button-nav {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      width: 200px;

      .btn-3 {
        span {
          padding: 10px 15px;
          background-color: $primary-color;
          border: 3px solid $primary-color;
          border-radius: 5px;
          color: white;
          transition: background 400ms;
        }
        &:hover {
          cursor: pointer;
          span {
            background-color: rgba(255, 255, 255, 0.1);
          }
        }
      }

      .profil {
        img {
          transition-duration: 500ms;
        }
        &:hover {
          cursor: pointer;
          img {
            transform: scale(1.2);
          }
        }
      }
    }
  }

  .container-body {
    padding: 20px 50px;

    .container-configured {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;
      align-items: center;
      padding: 20px;
    }
  }

</style>