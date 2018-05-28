
class ApiError extends Error {
  constructor(err, details = {}) {
    super();

    const { code, message } = err || DEFAULT;

    this.code = code;
    this.message = message;
    Error.captureStackTrace(this, this.constructor);
  }

  static isType(err, ...types) {
    return err instanceof ApiError && types.some(t => err.code === t.code);
  }
}

const ERRORS = {
  USER_EXISTS: { code: 1000, message: 'Email address already in use' },
  USER_NOT_FOUND: { code: 1001, message: 'Email address not registered' },
  PASSWORD_INCORRECT: { code: 1002, message: 'Password is incorrect' },
}

module.exports.ERRORS = ERRORS;
module.exports.ApiError = ApiError;
