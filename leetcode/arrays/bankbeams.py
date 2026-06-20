def numberOfBeams(bank: list[str]) -> int:
    numBeams = 0

    if len(bank) == 0 or len(bank) == 1:
        return 0

    for row in list(range(len(bank)-1)):
        devicesInCurrentRow = bank[row].count('1')
        if devicesInCurrentRow == 0:
            continue

        for nextRow in list(range(row+1, len(bank))):
            devicesInNextRow = bank[nextRow].count('1')
            if devicesInNextRow == 0:
                continue

            numBeams += devicesInCurrentRow * devicesInNextRow
            break

    return numBeams