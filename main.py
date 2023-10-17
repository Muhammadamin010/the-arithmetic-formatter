def arithmetic_arranger(problems, con=False):
    if len(problems) > 5:
        raise ValueError('Too many problems.')

    fline = ""
    sline = ""
    tline = ""
    aline = ""

    for problem in problems:
        problem = problem.strip()
        foper, opera, soper = problem.split()

        if len(foper) > 4 or len(soper) > 4:
            raise ValueError('Numbers cannot be more than four digits.')
        if opera not in ('+', '-'):
            raise ValueError('Operator must be \'+\' or \'-\'.')

        try:
            a = int(foper)
            b = int(soper)
        except ValueError:
            raise ValueError('Numbers must only contain digits.')

        if opera == '+':
            res = str(a + b)
        elif opera == '-':
            res = str(a - b)

        long = max(len(foper), len(soper))

        fline += foper.rjust(long + 2) + '    '
        sline += opera + soper.rjust(long + 1) + '    '
        tline += '-' * (long + 2) + '    '
        aline += res.rjust(long + 2) + '    '

    arranged_problems = fline.rstrip() + '\n' + sline.rstrip() + '\n' + tline.rstrip()

    if con:
        arranged_problems += '\n' + aline.rstrip()

    return arranged_problems

