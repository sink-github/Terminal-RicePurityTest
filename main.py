questions = [
    "Held hands romantically?\n",
    "Been on a date?",
    "Been in a relationship?",
    "Danced without leaving room for Jesus?",
    "Kissed a non-family member?",
    "Kissed a non-family member on the lips?",
    "French kissed?",
    "French kissed in public?",
    "Kissed on the neck?",
    "Kissed horizontally?",
    "Given or received a hickey?",
    "Kissed or been kissed on the breast?",
    "Kissed someone below the belt?",
    "Kissed for more than two hours consecutively?",
    "Played a game involving stripping?",
    "Seen or been seen by another person in a sensual context?",
    "Masturbated?",
    "Masturbated to a picture or video?",
    "Masturbated while someone else was in the room?",
    "Been caught masturbating?",
    "Masturbated with an inanimate object?",
    "Seen or read pornographic material?",
    "Massaged or been massaged sensually?",
    "Gone through the motions of intercourse while fully dressed?",
    "Undressed or been undressed by a MPS (member of the preferred sex)?",
    "Showered with a MPS?",
    "Fondled or had your butt cheeks fondled?",
    "Fondled or had your breasts fondled?",
    "Fondled or had your genitals fondled?",
    "Had or given \"blue balls\"?",
    "Had an orgasm due to someone else’s manipulation?",
    "Sent a sexually explicit text or instant message?",
    "Sent or received sexually explicit photographs?",
    "Engaged in sexually explicit activity over video chat?",
    "Cheated on a significant other during a relationship?",
    "Purchased contraceptives?",
    "Gave oral sex?",
    "Received oral sex?",
    "Ingested someone else's genital secretion?",
    "Used a sex toy with a partner?",
    "Spent the night with a MPS?",
    "Been walked in on while engaging in a sexual act?",
    "Kicked a roommate out to commit a sexual act?",
    "Ingested alcohol in a non-religious context?",
    "Played a drinking game?",
    "Been drunk?",
    "Faked sobriety to parents or teachers?",
    "Had severe memory loss due to alcohol?",
    "Used tobacco?",
    "Used marijuana?",
    "Used a drug stronger than marijuana?",
    "Used methamphetamine, crack cocaine, PCP, horse tranquilizers or heroin?",
    "Been sent to the office of a principal, dean or judicial affairs representative for a disciplinary infraction?",
    "Been put on disciplinary probation or suspended?",
    "Urinated in public?",
    "Gone skinny-dipping?",
    "Gone streaking?",
    "Seen a stripper?",
    "Had the police called on you?",
    "Run from the police?",
    "Had the police question you?",
    "Had the police handcuff you?",
    "Been arrested?",
    "Been convicted of a crime?",
    "Been convicted of a felony?",
    "Committed an act of vandalism?",
    "Had sexual intercourse?",
    "Had sexual intercourse three or more times in one night?",
    "?",
    "Had sexual intercourse 10 or more times?",
    "Had sexual intercourse in four or more positions?",
    "Had sexual intercourse with a stranger or person you met within 24 hours?",
    "Had sexual intercourse in a motor vehicle?",
    "Had sexual intercourse outdoors?",
    "Had sexual intercourse in public?",
    "Had sexual intercourse in a swimming pool or hot tub?",
    "Had sexual intercourse in a bed not belonging to you or your partner?",
    "Had sexual intercourse while you or your partner’s parents were in the same home?",
    "Had sexual intercourse with non-participating third party in the same room?",
    "Joined the mile high club?",
    "Participated in a \"booty call\” with a partner whom you were not in a relationship with?",
    "Traveled 100 or more miles for the primary purpose of sexual intercourse?",
    "Had sexual intercourse with a partner with a 3 or more year age difference?",
    "Had sexual intercourse with a virgin?",
    "Had sexual intercourse without a condom?",
    "Had a STI test due to reasonable suspicion?",
    "Had a STI?",
    "Had a threesome?",
    "Attended an orgy?",
    "Had two or more distinct acts of sexual intercourse with two or more people within 24 hours?",
    "Had sexual intercourse with five or more partners?",
    "Been photographed or filmed during sexual intercourse by yourself or others?",
    "Had period sex?",
    "Had anal sex?",
    "Had a pregnancy scare?",
    "Impregnated someone or been impregnated?",
    "Paid or been paid for a sexual act?",
    "Committed an act of voyeurism?",
    "Committed an act of incest?",
    "Engaged in bestiality?",
]


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


finished = 0
score = 100
cancelled = False
print(colored(0, 128, 0,
              "The Purity Test has historically served as a segue from O-week to true college life at Rice.\n" +
              "It's a voluntary opportunity for O-week groups to bond, and for students to track the maturation.\n" +
              "of their experiences throughout college.\n\n"))
print(colored(0, 128, 0, "Caution: This is not a bucket list. Completion of all items on this test will likely result "
                         "in death.\n"))
print(colored(0, 128, 0, "Click on every item you have done. MPS stands for Member of the Preferred Sex.\n"))
print("   ")
print(colored(0, 128, 0, "Please write \"y\" to check the prompt. Otherwise, write \"n\" to continue."))
while finished < 100 and cancelled is False:
    prompt = input(questions[finished] + ": ")
    if prompt.lower() == "yes" or prompt.lower() == "y":
        score -= 1
        finished += 1
        print("Total Score:", score)
    elif prompt.lower() == "cancel":
        cancelled = True
        score = 100
        finished = 0
        print("You have cancelled the program.")
    elif prompt.lower() == "no" or prompt.lower() == "n":
        finished += 1
        print("Total Score:", score)

if cancelled is False:
    print("Your Total Rice Purity Score:", score)
