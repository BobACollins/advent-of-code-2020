import re

expected_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

with open('problem_data.txt') as file:
    current_passport = {}
    passports = []
    for line in file:
        results = re.findall("[a-z]{3}:[^\s]+", line)
        if len(results) == 0:
            passports.append(current_passport)
            current_passport = {}
            continue
        for data in results:
            key, value = data.split(":")
            current_passport[key] = value
    passports.append(current_passport)
    count = 0
    count2 = 0
    print(passports)
    for passport in passports:
        if expected_keys.issubset(passport.keys()):
            count += 1
            try:
                byr = int(passport.get("byr", 0))
                if 2002 < byr or 1920 > byr:
                    raise ValueError()
                iyr = int(passport.get("iyr", 0))
                if 2010 > iyr or iyr > 2020:
                    raise ValueError()
                eyr = int(passport.get("eyr", 0))
                if 2020 > eyr or 2030 < eyr:
                    raise ValueError()
                hgt = passport.get("hgt")
                unit = hgt[-2:]
                height = int(hgt[:-2])
                if unit == "in" and 59 <= height <= 76:
                    pass
                elif unit == "cm" and 150 <= height <= 193:
                    pass
                else:
                    raise ValueError()
                result = passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]
                result &= re.match("^\d{9}$", passport["pid"]) is not None
                result &= re.match("^#[0-9a-f]{6}$", passport["hcl"]) is not None
                if result:
                    count2 += 1
                    # print(f"byr: {byr}")
                    # print(f"hgt: {hgt}")
                    # print(f"hcl: {passport['hcl']}")
                    # print(f"pid: {passport['pid']}")
                    print(f"iyr: {iyr}")
                    # print(f"eyr: {eyr}")
            except ValueError as e:
                continue
    print(f"First level is {count} our of {len(passports)}")
    print(f"Second level is {count2} our of {len(passports)}")