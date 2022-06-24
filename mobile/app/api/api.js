//////////// CONNECTION ////////////

const loginServer = (link, body, navigation) => {
    return fetch(link, {
        method: 'POST',
        body: body
    }
    )
    .then(response => response.json())
    .then(response => {
        global.connectUsername = response.username
        global.connectToken = response.token
        global.connectEmail = response.email
        if (response.username != "")
            navigation.navigate('ConfigService')
    }).catch((err) => console.log(err));
};

const loginServerGoogle = (link, body, navigation) => {
    return fetch(link, {
        method: 'POST',
        body: body
    }
    )
    .then(response => response.json())
    .then(response => {
        global.connectUsername = response.username
        global.connectToken = response.token
        global.connectEmail = response.email
        navigation.navigate('ConfigService')
    }).catch((err) => console.log(err));
};

const logoutServer = (link) => {
    return fetch(link, {
        method: 'POST',
        headers: {'Authorization': `Token ${global.connectToken}`},
    }
    )
    .then(response => response.json())
    .then(response => {
        global.connectUsername = ""
        global.connectToken = ""
        global.connectEmail = ""
        console.log("successfuly loged out !")
    }).catch((err) => console.log(err));
};

const connectGoogle = (link, body) => {
    return fetch(link, {
        headers: {'Authorization': `Bearer ${token}`},
        method: 'POST',
        body: body
    }
    )
    .then(response => response.json())
    .then(response => {
        console.log(response)
    }).catch((err) => console.log(err));
};

const createUser = (link, body) => {
    return fetch(link, {
        method: 'POST',
        body: body
    }
    )
    .then(response => response.json())
    .then(response => {
        global.registeredUser = response.username
        console.log(response)
    }).catch((err) => console.log(err));
};

const getServices = (link) => {
    return fetch(link, {
        headers: {'Authorization': `token ${global.connectToken}`},
        method: 'POST',
    }
    )
    .then(response => response.json())
    .then(response => {
        console.log(response)
    }).catch((err) => console.log(err));
};

export { loginServer, logoutServer, connectGoogle, createUser, getServices, loginServerGoogle };