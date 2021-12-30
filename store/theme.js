export const state = () => ({
  isDark: false,
})

export const actions = {
  getLocalTheme({ commit, state }) {
    if (
      localStorage.theme === 'dark' ||
      (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
    ) {
      commit('darkModeOn')
    } else {
      commit('lightModeOn')
    }
  },
}

export const mutations = {
  darkModeOn(state) {
    state.isDark = true
    localStorage.theme = 'dark'
    document.documentElement.classList.add('dark')
  },

  lightModeOn(state) {
    state.isDark = false
    localStorage.theme = 'light'
    document.documentElement.classList.remove('dark')
  },
}
