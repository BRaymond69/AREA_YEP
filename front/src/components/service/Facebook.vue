<template>
    <div class="facebook">
        <h1>Facebook Service Configured</h1>
        <a @click="sender()" class="btn-1"><span>Delete Service</span></a>
    </div>
</template>

<script>
//import axiosGet from '@/assets/script/api.js' 

export default {
    name: 'Fbconfigured',
    data () {
        return {
            username: '',
            password: '',
            error: '',
        }
    },
    methods: {
        async sender () {
            console.log('send delete')
            this.$emit('update-service')
        }
    },
    filters: {
    },
    mounted () {
    },
}
</script>

<style scoped lang="scss">

.facebook {
    display: flex;
    flex-flow: column wrap;
    justify-content: space-around;
    align-items: center;
    height: 200px;
    width: 200px;
    padding: 10px;
    background-color: white;
    border: 1px solid lightgrey;
    box-shadow: 0px 5px 19px 1px rgba(156,152,152,0.75);
    -webkit-box-shadow: 0px 5px 19px 1px rgba(156,152,152,0.75);
    -moz-box-shadow: 0px 5px 19px 1px rgba(156,152,152,0.75);
    border-radius: 10px;
}

</style>