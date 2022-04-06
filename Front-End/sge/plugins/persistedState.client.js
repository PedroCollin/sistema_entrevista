import createPersistedState from 'vuex-persistedstate'

export default ({ store }) => {
  createPersistedState({
    key: 'vuex',
    paths: ['user_session'],
  })(store),
  createPersistedState({
    key: 'jwt',
    paths: ['token'],
  })(store)
}