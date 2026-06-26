module.exports = {
  testEnvironment: 'node',
  collectCoverage: true,
  coverageDirectory: 'coverage',
  collectCoverageFrom: [
    'templates/nodejs/**/*.js',
  ],
  testMatch: ['**/tests/nodejs/**/*.test.js'],
};
