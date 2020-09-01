#This a modified file from MPT by Chronoshag https://www.reddit.com/user/chronoshag/
#It is part of the Mod "Time of Day effects for DDLC Mood Posing Tool"
#Created by me LordBaaa https://github.com/LordBaaa/
#If used or if the code from LayeredTime.rpy is used please credit me

layeredimage sayori turned: #turned definitions.
    group time:
    
        #LordBaaa
        attribute invert :
            se(invert_matrix) 
            
        #Koya-Sato
        attribute dawn:
            se(dawn_matrix) 
        attribute dawn2:
            se(dawn2_matrix)
            
        attribute morning:
            se(morning_matrix)
        attribute morning2:
            se(morning2_matrix)
            
        attribute sunset:
            se(sunset_matrix)
        attribute sunset2:
            se(sunset2_matrix) 
            
        attribute evening:
            se(evening_matrix)
        attribute evening2:
            se(evening2_matrix)
            
        attribute night:
            se(night_matrix)
        attribute night2:
            se(night2_matrix)
            
    always siwf("mod_assets/MPT/sayori/sayori_turned_facebase.png") #Always need this face.
    
    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: #Have to separate these out, they can't share moods.
        attribute nobl null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
    
    
    
    #Left arm variants
    group left if_any(["uniform"]):
        attribute ldown default:
            siwf("mod_assets/MPT/sayori/sayori_turned_uniform_left_down.png")
        attribute lup:
            siwf("mod_assets/MPT/sayori/sayori_turned_uniform_left_up.png")
    
    group left if_any(["casual"]):
        attribute ldown default:
            siwf("mod_assets/MPT/sayori/sayori_turned_casual_left_down.png")
        attribute lup:
            siwf("mod_assets/MPT/sayori/sayori_turned_casual_left_up.png")
    
    
    
    #Right arm variants
    group right if_any(["uniform"]):
        attribute rdown default:
            siwf("mod_assets/MPT/sayori/sayori_turned_uniform_right_down.png")
        attribute rup:
            siwf("mod_assets/MPT/sayori/sayori_turned_uniform_right_up.png")
    
    group right if_any(["casual"]):
        attribute rdown default:
            siwf("mod_assets/MPT/sayori/sayori_turned_casual_right_down.png")
        attribute rup:
            siwf("mod_assets/MPT/sayori/sayori_turned_casual_right_up.png")
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n1.png")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n2.png")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n3.png")
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n4.png")
        
        
        #All noses - truncated tags:
        attribute n1:
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n1.png")
        attribute n2:
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n2.png")
        attribute n3:
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n3.png")
        attribute n4:
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_n4.png")
        attribute nl:
            siwf("mod_assets/MPT/sayori/sayori_turned_nose_nl.png")
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_ma.png")
        attribute cm default if_any(["neut","anno","worr","curi"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_md.png")
        attribute cm default if_any(["dist","flus"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_me.png")
        attribute cm default if_any(["lsur","shoc"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mf.png")
        attribute cm default if_any(["sad","angr","pout","doub"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mj.png")
        attribute cm default if_any(["cry","pani","vsur"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mk.png")
        attribute cm default if_any(["vang"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mm.png")
        attribute cm default if_any(["laug"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mn.png")
        attribute cm default if_any(["yand"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mo.png")
        
        #Open Mouths:
        attribute om if_any(["happ","laug"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mb.png")
        attribute om if_any(["yand","nerv"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mc.png")
        attribute om if_any(["pout","sedu"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mf.png")
        attribute om if_any(["sad","lsur","dist"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mg.png")
        attribute om if_any(["neut","anno","shoc","worr"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mh.png")
        attribute om if_any(["curi","doub"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mi.png")
        attribute om if_any(["flus"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mk.png")
        attribute om if_any(["cry","vsur"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_ml.png")
        attribute om if_any(["angr","pani","vang"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mq.png")
        
        
        ###All mouths - truncated tags:
        attribute ma:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_ma.png")
        attribute mb:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mb.png")
        attribute mc:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mc.png")
        attribute md:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_md.png")
        attribute me:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_me.png")
        attribute mf:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mf.png")
        attribute mg:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mg.png")
        attribute mh:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mh.png")
        attribute mi:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mi.png")
        attribute mj:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mj.png")
        attribute mk:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mk.png")
        attribute ml:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_ml.png")
        attribute mm:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mm.png")
        attribute mn:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mn.png")
        attribute mo:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mo.png")
        attribute mp:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mp.png")
        attribute mq:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mq.png")
        attribute mr:
            siwf("mod_assets/MPT/sayori/sayori_turned_mouth_mr.png")
    
    
    
    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","angr","happ","laug","sad"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png")
        attribute oe default if_any(["dist","worr","pout"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png")
        attribute oe default if_any(["anno","sedu","doub"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png")
        attribute oe default if_any(["cry"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png")
        attribute oe default if_any(["lsur","flus","vsur","curi"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png")
        attribute oe default if_any(["nerv"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png")
        attribute oe default if_any(["pani","vang","shoc"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png")
        attribute oe default if_any(["yand"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png")
        
        #Default Closed eyes:
        attribute ce if_any(["sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png")
        attribute ce if_any(["neut","happ","lsur","laug","vsur","yand","pout","sedu"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png")
        attribute ce if_any(["vang","flus","pani"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png")
        attribute ce if_any(["cry"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png")
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png")
        attribute e1b:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png")
        attribute e1c:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1c.png")
        attribute e1d:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png")
        attribute e1e:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1e.png")
        attribute e1f:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1f.png")
        attribute e1g:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png")
        attribute e1h:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e1h.png")
        attribute e2a:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png")
        attribute e2b:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png")
        attribute e2c:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e2c.png")
        attribute e2d:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png")
        attribute e3a:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png")
        attribute e3b:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e3b.png")
        attribute e4a:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png")
        attribute e4b:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png")
        attribute e4c:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png")
        attribute e4d:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png")
        attribute e4e:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e4e.png")
        attribute e0a:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e0a.png")
        attribute e0b:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyes_e0b.png")
    
    
    
    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","flus","shoc"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png")
        attribute brow default if_any(["sad","cry","pani","yand","nerv"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png")
        attribute brow default if_any(["laug","vsur","worr","sedu"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png")
        attribute brow default if_any(["anno","pout"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png")
        attribute brow default if_any(["angr","vang"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png")
        attribute brow default if_any(["curi","doub"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png")
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png")
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png")
        
        
        ###All eyebrows - truncated tags:
        attribute b1a:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png")
        attribute b1b:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png")
        attribute b1c:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png")
        attribute b1d:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png")
        attribute b1e:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png")
        attribute b1f:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png")
        attribute b2a:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png")
        attribute b2b:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b2b.png")
        attribute b2c:
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b2c.png")
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b3a.png")
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b3b.png")
        attribute b3c if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            siwf("mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png")
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
        
        attribute s_scream:
            siwf("mod_assets/MPT/sayori/sayori_turned_special_scream.png")



layeredimage sayori tap: #tapping definitions.
    group time:

        #LordBaaa
        attribute invert :
            se(invert_matrix) 
            
        #Koya-Sato
        attribute dawn:
            se(dawn_matrix) 
        attribute dawn2:
            se(dawn2_matrix)
            
        attribute morning:
            se(morning_matrix)
        attribute morning2:
            se(morning2_matrix)
            
        attribute sunset:
            se(sunset_matrix)
        attribute sunset2:
            se(sunset2_matrix) 
            
        attribute evening:
            se(evening_matrix)
        attribute evening2:
            se(evening2_matrix)
            
        attribute night:
            se(night_matrix)
        attribute night2:
            se(night2_matrix)
            
    group outfit:
        attribute uniform default:
            siwf("mod_assets/MPT/sayori/sayori_tapping_uniform_bodybase.png")
        attribute casual:
            siwf("mod_assets/MPT/sayori/sayori_tapping_casual_bodybase.png")
    
    always siwf("mod_assets/MPT/sayori/sayori_tapping_facebase.png")
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute nerv default null #nervous
        attribute angr null #angry
        attribute dist null #distant
        attribute neut null #neutral
        attribute pout null #pouting
    
    
    
    group blush: #Have to separate these out, they can't share moods.
        attribute nobl default null #no blush applied.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n1.png")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n2.png")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n3.png")
        attribute nose default if_any(["blaw"]):#default nose when "blushing" and "awkward"
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n4.png")
        attribute nose default if_any(["bful"]):#default nose when "blushing" and "awkward"
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n5.png")
        
        #All noses - truncated tags:
        attribute n1:
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n1.png")
        attribute n2:
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n2.png")
        attribute n3:
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n3.png")
        attribute n4:
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n4.png")
        attribute n5:
            siwf("mod_assets/MPT/sayori/sayori_tapping_nose_n5.png")
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["pout"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png")
        attribute cm default if_any(["neut","nerv","angr","dist"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png")
        
        #Open Mouths:
        attribute om if_any(["nerv"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png")
        attribute om if_any(["neut","pout","angr","dist"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png")
        
        
        #All mouths - truncated tags:
        attribute m1:
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png")
        attribute m2:
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png")
        attribute m3:
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png")
        attribute m4:
            siwf("mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png")
    
    
    
    group eyes if_not(["n5","bful"]):
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","nerv"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png")
        attribute oe default if_any(["pout","dist"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png")
        attribute oe default if_any(["angr"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png")
        
        #Default Closed eyes:
        attribute ce if_any(["neut","nerv","pout","angr","dist"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png")
        
        
        #All eyes - truncated tags:
        attribute e1:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png")
        attribute e2:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png")
        attribute e3:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e3.png")
        attribute e4:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e4.png")
        attribute e5:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png")
        attribute e6:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png")
    
    
    
    group eyebrows if_not(["n5","bful"]):
        
        #Default Eyebrows:
        attribute brow default if_any(["neut"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png")
        attribute brow default if_any(["nerv","dist"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png")
        attribute brow default if_any(["pout","angr"]):
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png")
        
        
        #All eyebrows - truncated tags:
        attribute b1:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png")
        attribute b2:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png")
        attribute b3:
            siwf("mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png")



