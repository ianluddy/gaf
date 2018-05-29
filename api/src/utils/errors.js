
export class ApiError extends Error {
  constructor(err) {
    super();

    const { code, message } = err;

    this.code = code;
    this.message = message;
    Error.captureStackTrace(this, this.constructor);
  }

  static isType(err, ...types) {
    return err instanceof ApiError && types.some(t => err.code === t.code);
  }
}

export const ERRORS = {
  USER_EXISTS: { code: 1000, message: 'Email address already in use' },
  USER_NOT_FOUND: { code: 1001, message: 'Email address not registered' },
  PASSWORD_INCORRECT: { code: 1002, message: 'Password is incorrect' },
};
