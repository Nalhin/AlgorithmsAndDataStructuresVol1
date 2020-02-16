module.exports = {
  transform: {
    '^.+\\.tsx?$': 'ts-jest',
  },
  testRegex: '/__tests__/.*\\.(ts|tsx|js)$',
  collectCoverageFrom: ['src/**/*.{ts,tsx,js}'],
  preset: 'ts-jest',
};
