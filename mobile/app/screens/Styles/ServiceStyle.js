import { StyleSheet, Dimensions } from 'react-native';
const {width: WIDTH} = Dimensions.get('window');

export const ServiceStyle = StyleSheet.create({

    container: {
        flex: 1,
    },

    containerText: {
        color: 'white',
    },

    backgroundImage: {
        flex: 1,
        width: null,
        height: null,
        backgroundColor: '#000',
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
        fontWeight: 'bold',
        marginTop: '6%',
        opacity: 1,
        textAlign: 'center',
        alignItems: 'center',
        marginLeft: 20,
    },

    logoText2: {
        color: 'white',
        fontSize: 20,
        fontWeight: 'bold',
        opacity: 1,
        textAlign: 'center',
        alignItems: 'center',
    },

    goBack: {
        position: 'absolute',
        marginTop: '5%',
        marginLeft: '5%',
    },

    listItem: {
        margin: 20,
        padding: 20,
        backgroundColor: "#FFF",
        width: "80%",
        flex: 1,
        alignSelf: "center",
        flexDirection: "row",
        borderRadius: 5,
        maxWidth: 350,
    },

    Header: {
        marginTop: 30,
        flexDirection: 'row',
        marginBottom: 20,
    },
})