module.exports = {
    transform: {"^.+\\.tsx?$": "ts-jest",},
    testRegex: "/tests/.*\\.(ts|tsx|js)$",
    collectCoverageFrom: ["src/**/*.{ts,tsx,js}"],
    preset: "ts-jest",
}
