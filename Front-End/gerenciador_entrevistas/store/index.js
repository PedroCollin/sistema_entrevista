
//STATE
export const state = () => ({
    user_session: {},
    token : "",
    delay: 0,
})

//GETTERS
export const getters = {
    user_session(state){
        return state.user_session
    },

}

//ACTIONS
export const actions = {
    setUser_Session(context, payload) {
		context.commit("STORE_SESSION", payload);
	},

    //traz o usuario logado
	getUser(context) {
		return this.$axios.$get("/user").then((response) => {
			const content = response;
			if (content.detail == "Deslogado!") {
				this.message = "Not Logged";
				console.log("deu errado");
			} else {
				// this.$store.commit('user/STORE_SESSION', content)
				context.commit("STORE_SESSION", content);
				// console.log(this.$store.state.user.user_session)
				this.message = "Logged";
				console.log("deu certo");
			}
			return response;
		});
	},


	delay(context, payload) {
		context.commit("DELAY", payload);
	},

}

//MUTATIONS
export const mutations = {
    STORE_SESSION(state, payload){
        state.user_session = payload;
    },

    STORE_TOKEN(state, payload){
        state.token = payload;
    },

    DELAY(state, payload){
        state.delay = payload;
    }
}
