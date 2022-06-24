import { StyleSheet, Dimensions } from 'react-native';
const {width: WIDTH} = Dimensions.get('window')

export const LoginStyle = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        color: '#fff',
    },

    containerText: {
        color: 'white',
    },

    backgroundImage: {
        flex: 1,
        width: null,
        height: null,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#667',
    },

    logoContainer: {
        alignItems: 'center',
        marginBottom: 50,
    },

    logo: {
        marginTop: 32,
        marginBottom: 16,
        width: 64,
        height: 64,
    },

    logoText: {
        color: 'white',
        fontSize: 20,
        fontWeight: '600',
        marginTop: 15,
        opacity: 0.5,
    },

    inputContainer: {
        marginTop: 10,
        marginBottom: 10,
    },
    input: {
        width:  WIDTH / 1.5,
        height: 45,
        borderRadius: 40,
        fontSize: 15,
        paddingLeft: 45,
        backgroundColor: 'rgba(0,0,0,0.35)',
        color: 'rgba(255,255,255,0.7)',
        marginHorizontal: 25,
    },

    inputIcon: {
        position: 'absolute',
        top: 7,
        left: 35,
    },

    eyeBtn: {
        position: 'absolute',
        top: 7,
        right: 40,
    },

    loginBtn:{
        width:  WIDTH / 4,
        height: 45,
        borderRadius: 40,
        fontSize: 15,
        backgroundColor: '#432577',
        justifyContent: 'center',
        marginTop: 20,
    },

    text: {
        color: 'rgba(255,255,255,0.7)',
        fontSize: 16,
        textAlign: 'center',
    },

    googleContainer: {
        width: 240,
        height: 50,
    },
    googleIcon: {
        marginTop: 20,
        alignItems: 'center',
    },
})