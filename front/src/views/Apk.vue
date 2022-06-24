<template>
    <div>
        <a id="downloaded" :href="publicPath + 'app-release.apk'" download="app-release.apk"></a>
    </div>
</template>

<script>

export default {
    name: 'Apk',
    data () {
    return {
        publicPath: process.env.BASE_URL
    }
    },
    methods: {
    },
    filters: {
    },
    mounted () {
        let link = document.getElementById('downloaded')
        link.click()
    },
}
</script>

<style scoped lang="scss">

</style>