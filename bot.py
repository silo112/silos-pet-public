import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "-")

@bot.event
async def on_ready():
    print('Ready to rock!')
    await bot.change_presence(activity=discord.Game(name='with your lives.'))

#CATEGORIES
def valid_users(ctx):
    return ctx.author.id == 332679373142491136,230187378281676800

def valid_channels(ctx):
    return ctx.channel.id == 757757276105998346

#RESET MESSAGES
@bot.command()
@commands.check(valid_users)
async def reset(ctx):
    rp_rooms = [747139969323106345,747139999866028082,747140943823765534,747141043602063501,747141096697757826,747141164066406510,747141215962792126,747141267275644989,747141313287421984,747141363996295179,747141438336270346,747141807673966663,747143305560850513,747143326276386916,747143407343894628,747143455959941251,747143500985925713,747143607403937822,747143734637887490,747143868998221835,747144010472357959,747144076838699099,747144135005175918,747144181750693979,747144575273009304,747144945001037841,747144986226720849,747145025972076626,747145100940804246,747145145434243305,747145431179591831,747145499726970961,747145549177946242,747145595583594666,747146165061025832,747146209319321671,747146247562985472,747146289942233119,747146451137724577,747165971172818975,747164775753973874,747164809337897030,747164881924522095,748708937485778965,798205461307850772,798215221570437150,752178559971491902,752179723311906886,747181344844415089,747181390868512849,747181412922294432,747181474964570234,758023894983508089,822425929586180126,830984714734272582,830984671427821608,837130783298027520,830984282377551883,830983492908220446,830983474369527828,830983445684682832,830983143754170368,898216592733790228,841077511571636254,889468667824308254,847547500356567140,956460897587593266,954329271365693440.]
    for room in rp_rooms:
        await bot.get_channel(room).send("**It's a new day/night!** The server has been **reset**, which means everyone went back to their homes to sleep. If you have the 'no haven' flaw and found no place to stay(be it via rolls or RP) you took **sunlight damage** (Aggravated Health damage at the rate of your Bane Severity in points). Remember to do a rouse check for waking up and a remorse check if you have any stains. Also don't forget to include your **[Location - A or NA]** and **Rolls** in posts to get your **EXP**!")

@bot.command()
@commands.check(valid_users)
async def reboot(ctx):
    await bot.get_channel(760318182027427911).send("```Transferring..............................................................Content backed and erased. Server Going Offline```\n - \n ```Booting..............................................................Done! \n TPF is back online. Evening suckers.```")

#DISCIPLINES

#ANIMALISM
f = open("disciplines/bondfamulus.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def bond_famulus(ctx):
    await ctx.send(f.read())
    f.close()

f1 = open("disciplines/sensethebeast.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def sense_the_beast(ctx):
    await ctx.send(f1.read())
    f1.close()

f2 = open("disciplines/feralwhispers.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def feral_whispers(ctx):
    await ctx.send(f2.read())
    f2.close()

f3 = open("disciplines/animal_succulence.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def animal_succulence(ctx):
    await ctx.send(f3.read())
    f3.close()

f4 = open("disciplines/quell_the_beast.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def quell_the_beast(ctx):
    await ctx.send(f4.read())
    f4.close()

f5 = open("disciplines/unliving_hive.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def unliving_hive(ctx):
    await ctx.send(f5.read())
    f5.close()

f6 = open("disciplines/subsume_the_spirit.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def subsume_the_spirit(ctx):
    await ctx.send(f6.read())
    f6.close()

f7 = open("disciplines/animal_dominion.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def animal_dominion(ctx):
    await ctx.send(f7.read())
    f7.close()

f8 = open("disciplines/drawing_out_the_beast.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def drawing_out_the_beast(ctx):
    await ctx.send(f8.read())
    f8.close()

#AUSPEX
f9 = open("disciplines/heightened_senses.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def heightened_senses(ctx):
    await ctx.send(f9.read())
    f9.close()

f10 = open("disciplines/sense_the_unseen.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def sense_the_unseen(ctx):
    await ctx.send(f10.read())
    f10.close()

f11 = open("disciplines/premonition.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def premonition(ctx):
    await ctx.send(f11.read())
    f11.close()

f12 = open("disciplines/scry_the_soul.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def scry_the_soul(ctx):
    await ctx.send(f12.read())
    f12.close()

f13 = open("disciplines/share_the_senses.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def share_the_senses(ctx):
    await ctx.send(f13.read())
    f13.close()

f14 = open("disciplines/spirits_touch.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def spirits_touch(ctx):
    await ctx.send(f14.read())
    f14.close()

f15 = open("disciplines/clarivoyance.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def clarivoyance(ctx):
    await ctx.send(f15.read())
    f15.close()

f16 = open("disciplines/possession.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def possession(ctx):
    await ctx.send(f16.read())
    f16.close()

f17 = open("disciplines/telepathy.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def telepathy(ctx):
    await ctx.send(f17.read())
    f17.close()

#CELERITY
f18 = open("disciplines/cats_grace.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def cats_grace(ctx):
    await ctx.send(f18.read())
    f18.close()

f19 = open("disciplines/rapid_reflexes.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def rapid_reflexes(ctx):
    await ctx.send(f19.read())
    f19.close()

f20 = open("disciplines/fleetness.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def fleetness(ctx):
    await ctx.send(f20.read())
    f20.close()

f21 = open("disciplines/blink.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def blink(ctx):
    await ctx.send(f21.read())
    f21.close()

f22 = open("disciplines/traversal.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def traversal(ctx):
    await ctx.send(f22.read())
    f22.close()

f23 = open("disciplines/draught_of_elegance.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def draught_of_elegance(ctx):
    await ctx.send(f23.read())
    f23.close()

f24 = open("disciplines/unerring_aim.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def unerring_aim(ctx):
    await ctx.send(f24.read())
    f24.close()

f25 = open("disciplines/lightning_strike.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def lightning_strike(ctx):
    await ctx.send(f25.read())
    f25.close()

f26 = open("disciplines/split_second.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def split_second(ctx):
    await ctx.send(f26.read())
    f26.close()

#DOMINATE
f27 = open("disciplines/cloud_memory.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def cloud_memory(ctx):
    await ctx.send(f27.read())
    f27.close()

f28 = open("disciplines/compel.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def compel(ctx):
    await ctx.send(f28.read())
    f28.close()

f29 = open("disciplines/mesmerize.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def mesmerize(ctx):
    await ctx.send(f29.read())
    f29.close()

f30 = open("disciplines/dementation.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def dementation(ctx):
    await ctx.send(f30.read())
    f30.close()

f31 = open("disciplines/the_forgetful_mind.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def the_forgetful_mind(ctx):
    await ctx.send(f31.read())
    f31.close()

f32 = open("disciplines/submerged_directive.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def submerged_directive(ctx):
    await ctx.send(f32.read())
    f32.close()

f33 = open("disciplines/rationalize.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def rationalize(ctx):
    await ctx.send(f33.read())
    f33.close()

f34 = open("disciplines/mass_manipulation.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def mass_manipulation(ctx):
    await ctx.send(f34.read())
    f34.close()

f35 = open("disciplines/terminal_decree.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def terminal_decree(ctx):
    await ctx.send(f35.read())
    f35.close()

#FORTITUDE
f36 = open("disciplines/resilience.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def resilience(ctx):
    await ctx.send(f36.read())
    f36.close()

f37 = open("disciplines/unswayable_mind.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def unswayable_mind(ctx):
    await ctx.send(f37.read())
    f37.close()

f38 = open("disciplines/toughness.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def toughness(ctx):
    await ctx.send(f38.read())
    f38.close()

f39 = open("disciplines/enduring_beasts.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def enduring_beasts(ctx):
    await ctx.send(f39.read())
    f39.close()

f40 = open("disciplines/defy_bane.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def defy_bane(ctx):
    await ctx.send(f40.read())
    f40.close()

f41 = open("disciplines/fortify_the_inner_facade.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def fortify_the_inner_facade(ctx):
    await ctx.send(f41.read())
    f41.close()

f42 = open("disciplines/draught_of_endurance.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def draught_of_endurance(ctx):
    await ctx.send(f42.read())
    f42.close()

f43 = open("disciplines/flesh_of_marble.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def flesh_of_marble(ctx):
    await ctx.send(f43.read())
    f43.close()

f44 = open("disciplines/prowess_from_pain.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def prowess_from_pain(ctx):
    await ctx.send(f44.read())
    f44.close()

#OBFUSCATE
f45 = open("disciplines/cloak_of_shadows.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def cloak_of_shadows(ctx):
    await ctx.send(f45.read())
    f45.close()

f46 = open("disciplines/silence_of_death.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def silence_of_death(ctx):
    await ctx.send(f46.read())
    f46.close()

f47 = open("disciplines/unseen_passage.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def unseen_passage(ctx):
    await ctx.send(f47.read())
    f47.close()

f48 = open("disciplines/ghost_in_the_machine.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def ghost_in_the_machine(ctx):
    await ctx.send(f48.read())
    f48.close()

f49 = open("disciplines/mask_of_a_thousand_faces.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def mask_of_a_thousand_faces(ctx):
    await ctx.send(f49.read())
    f49.close()

f50 = open("disciplines/conceal.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def conceal(ctx):
    await ctx.send(f50.read())
    f50.close()

f51 = open("disciplines/vanish.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def vanish(ctx):
    await ctx.send(f51.read())
    f51.close()

f52 = open("disciplines/cloak_the_gathering.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def cloak_the_gathering(ctx):
    await ctx.send(f52.read())
    f52.close()

f53 = open("disciplines/impostors_guise.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def impostors_guise(ctx):
    await ctx.send(f53.read())
    f53.close()

#POTENCE
f54 = open("disciplines/lethal_body.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def lethal_body(ctx):
    await ctx.send(f54.read())
    f54.close()

f55 = open("disciplines/soaring_leap.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def soaring_leap(ctx):
    await ctx.send(f55.read())
    f55.close()

f56 = open("disciplines/prowess.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def prowess(ctx):
    await ctx.send(f56.read())
    f56.close()

f57 = open("disciplines/brutal_feed.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def brutal_feed(ctx):
    await ctx.send(f57.read())
    f57.close()

f58 = open("disciplines/spark_of_rage.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def spark_of_rage(ctx):
    await ctx.send(f58.read())
    f58.close()

f59 = open("disciplines/uncanny_grip.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def uncanny_grip(ctx):
    await ctx.send(f59.read())
    f59.close()

f60 = open("disciplines/draught_of_might.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def draught_of_might(ctx):
    await ctx.send(f60.read())
    f60.close()

f61 = open("disciplines/earthshock.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def earthshock(ctx):
    await ctx.send(f61.read())
    f61.close()

f62 = open("disciplines/fist_of_caine.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def fist_of_caine(ctx):
    await ctx.send(f62.read())
    f62.close()

#PRESENCE
f63 = open("disciplines/awe.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def awe(ctx):
    await ctx.send(f63.read())
    f63.close()

f64 = open("disciplines/daunt.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def daunt(ctx):
    await ctx.send(f64.read())
    f64.close()

f65 = open("disciplines/lingering_kiss.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def lingering_kiss(ctx):
    await ctx.send(f65.read())
    f65.close()

f66 = open("disciplines/dread_gaze.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def dread_gaze(ctx):
    await ctx.send(f66.read())
    f66.close()

f67 = open("disciplines/entrancement.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def entrancement(ctx):
    await ctx.send(f67.read())
    f67.close()

f68 = open("disciplines/irresistible_voice.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def irresistible_voice(ctx):
    await ctx.send(f68.read())
    f68.close()

f69 = open("disciplines/summon.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def summon(ctx):
    await ctx.send(f69.read())
    f69.close()

f70 = open("disciplines/majesty.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def majesty(ctx):
    await ctx.send(f70.read())
    f70.close()

f71 = open("disciplines/star_magnetism.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def star_magnetism(ctx):
    await ctx.send(f71.read())
    f71.close()

#PROTEAN
f72 = open("disciplines/eyes_of_the_beast.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def eyes_of_the_beast(ctx):
    await ctx.send(f72.read())
    f72.close()

f73 = open("disciplines/weight_of_the_feather.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def weight_of_the_feather(ctx):
    await ctx.send(f73.read())
    f73.close()

f74 = open("disciplines/feral_weapons.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def feral_weapons(ctx):
    await ctx.send(f74.read())
    f74.close()

f75 = open("disciplines/earth_meld.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def earth_meld(ctx):
    await ctx.send(f75.read())
    f75.close()

f76 = open("disciplines/shapechange.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def shapechange(ctx):
    await ctx.send(f76.read())
    f76.close()

f77 = open("disciplines/metamorphosis.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def metamorphosis(ctx):
    await ctx.send(f77.read())
    f77.close()

f78 = open("disciplines/mist_form.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def mist_form(ctx):
    await ctx.send(f78.read())
    f78.close()

f79 = open("disciplines/the_unfettered_heart.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def the_unfettered_heart(ctx):
    await ctx.send(f79.read())
    f79.close()

#BLOOD SORCERY
f80 = open("disciplines/corrosive_vitae.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def corrosive_vitae(ctx):
    await ctx.send(f80.read())
    f80.close()

f81 = open("disciplines/a_taste_for_blood.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def a_taste_for_blood(ctx):
    await ctx.send(f81.read())
    f81.close()

f82 = open("disciplines/extinguish_vitae.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def extinguish_vitae(ctx):
    await ctx.send(f82.read())
    f82.close()

f83 = open("disciplines/blood_of_potency.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def blood_of_potency(ctx):
    await ctx.send(f83.read())
    f83.close()

f84 = open("disciplines/scorpions_touch.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def scorpions_touch(ctx):
    await ctx.send(f84.read())
    f84.close()

f85 = open("disciplines/theft_of_vitae.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def theft_of_vitae(ctx):
    await ctx.send(f85.read())
    f85.close()

f86 = open("disciplines/baals_caress.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def baals_caress(ctx):
    await ctx.send(f86.read())
    f86.close()

f87 = open("disciplines/cauldron_of_blood.txt", encoding="utf8")
@bot.command()
@commands.check(valid_channels)
async def cauldron_of_blood(ctx):
    await ctx.send(f87.read())
    f87.close()

bot.run('private discord code goes here')
