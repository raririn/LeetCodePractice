int myAtoi(char* str) {
    int ret = 0;
    int sgn = 1;
    /* Check for null pointer */
    if (str == 0){
        return ret;
    }
    while (isspace(*str)){
        str++;
    }
    if (*str == '+' || *str == '-'){
        if (*str == '-'){
            sgn = -1;
        }
        str++;
    }

    while (isdigit(*str)){
        /* Convert a single string to integer: consider ASCII */
        int num = *str - '0';
        if (sgn == 1 && (ret > INT_MAX / 10 || (ret == INT_MAX / 10 && num > INT_MAX % 10))){
            return INT_MAX;
        }
        else if (sgn == -1 && (ret > (unsigned)INT_MIN / 10 || (ret == (unsigned) INT_MIN / 10 && num > (unsigned)INT_MIN % 10))){
            return INT_MIN;
        }
        ret = ret*10 + num;
        str++;
    }
    return sgn*ret;
}