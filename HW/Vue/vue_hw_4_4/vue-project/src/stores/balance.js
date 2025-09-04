import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', {
  state: () => ({
    balances: [
      { name: '김하나', balance: 100000 },
      { name: '김두리', balance: 10000 },
      { name: '김서이', balance: 100 },
    ],
  }),
  getters: {
    // 인자를 받는 getter (Pinia 공식문서 방식)
    byName: (state) => (name) => state.balances.find(b => b.name === name),
  },
  actions: {
    increment(name, amount = 1000) {
      const t = this.balances.find(b => b.name === name)
      if (t) t.balance += amount
    },
  },
})
