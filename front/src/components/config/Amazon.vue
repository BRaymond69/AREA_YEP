<template>
    <div class="facebook">
        <h1>Amazon Service</h1>
        <input type="text" v-model="username" placeholder="all or last ..." required>
        <p>{{error}}</p>
        <a @click="sender()" class="btn-0"><span>Start Service</span></a>
    </div>
</template>

<script>
import axiosGet from '@/assets/script/api.js' 

export default {
    name: 'Amazon',
    data () {
    return {
        username: '',
        error: '',
    }
    },
    methods: {
        async sender () {
            const params = {'amazonNumber': this.username}
            await axiosGet.post('/amazon/', params)
            .then((response) => {
                console.log(response)
                this.error = ''
                this.$emit('update-service')
            }).catch((error) => {
                console.log(error)
                this.error = 'Error: Bad argument'
            })
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
    height: 300px;
    width: 200px;
    padding: 10px;
    background-color: white;
    border: 1px solid lightgrey;
    box-shadow: 0px 5px 19px 1px rgba(156,152,152,0.75);
    -webkit-box-shadow: 0px 5px 19px 1px rgba(156,152,152,0.75);
    -moz-box-shadow: 0px 5px 19px 1px rgba(156,152,152,0.75);
    border-radius: 10px;
}

p {color: red;}

input {
    width: 80%;
    height: 30px;
    border: 1px solid lightgrey;
    padding: 5px;
    border-radius: 10px;
}

</style>