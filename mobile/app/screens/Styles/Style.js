import { StyleSheet, Dimensions } from 'react-native';
import { block } from 'react-native-reanimated';
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
        width:  WIDTH / 1.4,
        height: 45,
        borderRadius: 40,
        fontSize: 15,
        paddingLeft: 45,
        backgroundColor: 'rgba(0,0,0,0.35)',
        color: 'rgba(255,255,255,0.7)',
        marginHorizontal: 25,
    },
    inputConfig: {
        width:  WIDTH / 1.4,
        height: 45,
        borderRadius: 40,
        fontSize: 14,
        borderWidth: 1,
        paddingHorizontal: 5,
        borderColor: 'white',
        backgroundColor: 'rgba(0,0,0,0.35)',
        color: 'rgba(255,255,255,0.7)',
        marginHorizontal: 20,

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

    viewBtn: {
        flexDirection: 'row',
        justifyContent: 'center',
    },
    scrollView: {
        height: 1000,
    //    borderWidth: 2,
    //    borderColor: '#FFFFFF'
    },
    viewConfig: {
        justifyContent: 'center',
        borderWidth: 2,
        marginTop: 10,
        marginLeft: 30,
        borderColor: '#FFFFFF',
        width: 300,
    },
    loginBtn:{
        width:  WIDTH / 4,
        height: 45,
        borderRadius: 40,
        fontSize: 15,
        backgroundColor: '#432577',
        justifyContent: 'center',
        marginTop: 20,
        marginLeft: 10,
    },
    logoutBtn:{
        width:  WIDTH / 4,
        height: 45,
        borderRadius: 40,
        fontSize: 15,
        backgroundColor: '#FFFFFF',
        justifyContent: 'center',
        marginLeft: 10,
        marginBottom: 5,
        marginTop: 14,
    },
    Services:{
        width:  WIDTH / 4,
        height: 45,
        borderRadius: 40,
        fontSize: 15,
        backgroundColor: '#FFFFFF',
        justifyContent: 'center',
        marginLeft: 130,
        marginBottom: 5,
        marginTop: 14,
    },
    configBtn:{
        width:  WIDTH / 3.5,
        height: 45,
        borderRadius: 40,
        fontSize: 15,
        backgroundColor: '#63AA99',
        justifyContent: 'center',
        marginTop: 10,
        marginLeft: 90,
        marginBottom: 10,

    },
    text: {
        color: 'rgba(255,255,255,0.7)',
        fontSize: 16,
        textAlign: 'center',
    },
    textBlackOnWhite: {
        color: 'rgba(0,0,0,0.7)',
        fontSize: 16,
        textAlign: 'center',
    },
    googleContainer: {
        width: 240,
        height: 50,
    },
    logoGoogle: {
        textAlign: 'center',
        paddingTop: 10,
    },
})