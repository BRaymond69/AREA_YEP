<template>
    <div class="popup-profil">
        <a @click="open()" class="image-click"><img src="https://img.icons8.com/ios-glyphs/60/ffffff/user-male.png"/></a>
        <div id="bgpopup" v-show="on_click">
        <div class="popup" tabindex="0">
            <div class="close-button">
                <a @click="close()"><img src="https://img.icons8.com/windows/32/000000/macos-close.png"/></a>
            </div>
            <div class="image-preview">
                <h1>bernard</h1>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Profil',
    data () {
    return {
        on_preview: true,
        on_click: false,
    }
    },
    methods: {
        press_handler (event) {
            if (event.code === 'Escape')
                this.close()
        },
        click_handler (event) {
            if (event.target.id === 'bgpopup')
                this.close()
        },
        close () {
            this.on_click = false
            document.removeEventListener('click', this.click_handler, true)
            document.removeEventListener('keydown', this.press_handler, true)
        },
        open () {
            this.on_click = !this.on_click
            if (this.on_click) {
                document.addEventListener('click', this.click_handler, true)
                document.addEventListener('keydown', this.press_handler, true)
            }
        },
    },
    filters: {
    },
    mounted () {
        if (this.src.search('/static/assets/img/file_icon.svg') != -1)
            this.on_preview = false
    },
}
</script>

<style scoped lang="scss">
#bgpopup {
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    background-color: rgba(255, 255, 255, 0.8);
    z-index: 998;
}

.popup {
    width: 50vw;
    min-height: 25vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 10px;
    background-color: white;
    border: 1px solid lightgrey;
    z-index: 999;
}

.popup .close-button {
    display: flex;
    justify-content: flex-end;
    width: 100%;
    height: 1vh;
    top: 0;
}

.popup .close-button i {
    transform: scale(1.5);
    padding: 5px;
    transition-duration: 300ms;
}

.popup .close-button a {
    padding: 10px 15px;
}

.popup .close-button a:hover {
    cursor: pointer;
}

.popup .close-button a:hover i {
    background-color: #e6e4f5;
    border-radius: 50%;
}

.image-preview {
    min-height: 24vh;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-bottom: 1vh;
}
</style>