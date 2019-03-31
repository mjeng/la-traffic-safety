from point import Point
from grid import Grid
import all_scores


g = Grid(33.707, 34.3343, -118.1554, -118.6661, 0.009)
g.create_grid("data/cleaned_2018_data.csv", "pickle_test.p")

print("FINISHED MAKING GRID")

test = '["34.18704 -118.38125000000001", "34.186690000000006 -118.38125000000001", "34.186690000000006 -118.38125000000001", "34.186690000000006 -118.38178", "34.186690000000006 -118.38235000000002", "34.186690000000006 -118.38281", "34.186690000000006 -118.38343", "34.186690000000006 -118.38393", "34.186690000000006 -118.38506000000001", "34.186690000000006 -118.38533000000001", "34.18668 -118.38649000000001", "34.18668 -118.38671000000001", "34.18668 -118.38682000000001", "34.18668 -118.38695000000001", "34.18668 -118.38712000000001", "34.186690000000006 -118.38777", "34.186690000000006 -118.38808000000002", "34.18668 -118.38847000000001", "34.18668 -118.38864000000001", "34.18668 -118.38889", "34.18668 -118.38956", "34.18668 -118.38999000000001", "34.18668 -118.39065000000001", "34.18668 -118.39108000000002", "34.18668 -118.39169000000001", "34.18668 -118.39217000000001", "34.18667 -118.39271000000001", "34.186690000000006 -118.39287000000002", "34.186690000000006 -118.39326000000001", "34.186690000000006 -118.39373", "34.186690000000006 -118.39435", "34.18668 -118.39483000000001", "34.186690000000006 -118.39543", "34.18668 -118.39580000000001", "34.18668 -118.39646", "34.18668 -118.3966", "34.18668 -118.39713", "34.18668 -118.39779000000001", "34.18668 -118.39875", "34.186690000000006 -118.39942", "34.1867 -118.39946", "34.186710000000005 -118.39949000000001", "34.18672 -118.39953000000001", "34.186730000000004 -118.39958000000001", "34.186730000000004 -118.39963000000002", "34.18674 -118.39968", "34.18674 -118.39979000000001", "34.18674 -118.40026", "34.18674 -118.40051000000001", "34.18674 -118.40055000000001", "34.18674 -118.40058", "34.18675 -118.40061000000001", "34.18676 -118.40065000000001", "34.18675 -118.40107", "34.18675 -118.40276000000001", "34.18675 -118.40276000000001", "34.18677 -118.40276000000001", "34.186780000000006 -118.40277", "34.186800000000005 -118.40278", "34.18681 -118.40279000000001", "34.186840000000004 -118.40281000000002", "34.18686 -118.40283000000001", "34.186870000000006 -118.40284000000001", "34.186890000000005 -118.40285000000002", "34.1869 -118.40286", "34.18692 -118.40286", "34.186930000000004 -118.40287000000001", "34.18695 -118.40287000000001", "34.186960000000006 -118.40288000000001", "34.187000000000005 -118.40288000000001", "34.18703 -118.40288000000001", "34.18706 -118.40288000000001", "34.187310000000004 -118.40288000000001", "34.187670000000004 -118.40288000000001", "34.18775 -118.40288000000001", "34.187780000000004 -118.40288000000001", "34.1878 -118.40288000000001", "34.18782 -118.40288000000001", "34.18784 -118.40287000000001", "34.18786 -118.40287000000001", "34.18788 -118.40286", "34.187900000000006 -118.40285000000002", "34.187920000000005 -118.40284000000001", "34.187960000000004 -118.40281000000002", "34.187990000000006 -118.40278", "34.188010000000006 -118.40277", "34.18802 -118.40275000000001", "34.18804 -118.40272000000002", "34.18806 -118.40270000000001", "34.18807 -118.40268", "34.18808 -118.40266000000001", "34.18808 -118.40264", "34.18809 -118.40263000000002", "34.188100000000006 -118.4026", "34.18811 -118.40258000000001", "34.18811 -118.40256000000001", "34.18811 -118.40255", "34.18811 -118.40254000000002", "34.188120000000005 -118.40252000000001", "34.188120000000005 -118.40249000000001", "34.188120000000005 -118.40246", "34.188120000000005 -118.40242", "34.188120000000005 -118.40238000000001", "34.18811 -118.40235000000001", "34.188100000000006 -118.40233", "34.188100000000006 -118.40231000000001", "34.18808 -118.40227000000002", "34.18808 -118.40225000000001", "34.18807 -118.40224", "34.188050000000004 -118.40220000000001", "34.188030000000005 -118.40217000000001", "34.188010000000006 -118.40215", "34.188 -118.40213000000001", "34.187990000000006 -118.40212000000001", "34.18798 -118.4021", "34.187960000000004 -118.40209000000002", "34.18795 -118.40208000000001", "34.18793 -118.40207000000001", "34.18791 -118.40206", "34.187870000000004 -118.40204000000001", "34.187830000000005 -118.40202000000001", "34.1877 -118.40197", "34.18753 -118.40191000000002", "34.187400000000004 -118.40187000000002", "34.18714 -118.40178000000002", "34.18704 -118.40175", "34.187020000000004 -118.40173000000001", "34.187000000000005 -118.40173000000001", "34.18699 -118.40172000000001", "34.186980000000005 -118.40171000000001", "34.186980000000005 -118.40169000000002", "34.18697 -118.40167000000001", "34.18697 -118.40164000000001", "34.18697 -118.40159000000001", "34.18686 -118.40156", "34.18676 -118.40153000000001", "34.18657 -118.40147", "34.18638 -118.40139", "34.186170000000004 -118.40131000000001", "34.18598 -118.40122000000001", "34.18585 -118.40116", "34.18569 -118.40108000000001", "34.185520000000004 -118.40098", "34.185390000000005 -118.40090000000001", "34.185300000000005 -118.40085", "34.18506 -118.40069000000001", "34.18491 -118.40058", "34.18462 -118.40035", "34.18442 -118.40018", "34.18422 -118.40001000000001", "34.18399 -118.39977", "34.18385 -118.39962000000001", "34.18374 -118.39949000000001", "34.183420000000005 -118.39912000000001", "34.183310000000006 -118.39897", "34.18307 -118.39868000000001", "34.18276 -118.3983", "34.18249 -118.39797000000002", "34.18215 -118.39756000000001", "34.18193 -118.39730000000002", "34.181720000000006 -118.39708000000002", "34.181540000000005 -118.39690000000002", "34.18133 -118.39670000000001", "34.18103 -118.39643000000001", "34.18081 -118.39624", "34.18054 -118.39603000000001", "34.18019 -118.39578000000002", "34.180080000000004 -118.3957", "34.17973 -118.39548", "34.17965 -118.39543", "34.17945 -118.39532000000001", "34.17929 -118.39524000000002", "34.179080000000006 -118.39513000000001", "34.178580000000004 -118.39489", "34.177980000000005 -118.39459000000001", "34.177550000000004 -118.39439000000002", "34.177260000000004 -118.39425000000001", "34.17698 -118.39412000000002", "34.176520000000004 -118.39388000000001", "34.17642 -118.39382", "34.17616 -118.39367000000001", "34.17589 -118.39349000000001", "34.17564 -118.39331000000001", "34.17544 -118.39316000000001", "34.175250000000005 -118.39301", "34.175050000000006 -118.39284", "34.174820000000004 -118.39263000000001", "34.174620000000004 -118.39244000000001", "34.17447 -118.3923", "34.174350000000004 -118.39217000000001", "34.174260000000004 -118.39207", "34.174130000000005 -118.39194", "34.174060000000004 -118.39186000000001", "34.17387 -118.39163", "34.173660000000005 -118.39137000000001", "34.173480000000005 -118.39112000000002", "34.17338 -118.39098000000001", "34.17324 -118.39078", "34.17305 -118.39046", "34.17296 -118.39034000000001", "34.172520000000006 -118.38967000000001", "34.17239 -118.38949000000001", "34.17219 -118.38919000000001", "34.17203 -118.38894", "34.171890000000005 -118.38875000000002", "34.171600000000005 -118.38830000000002", "34.171490000000006 -118.38813", "34.17145 -118.38808000000002", "34.17127 -118.38781000000002", "34.1711 -118.38755", "34.17098 -118.38736000000002", "34.17063 -118.38683", "34.17056 -118.38673000000001", "34.170260000000006 -118.38632000000001", "34.170100000000005 -118.38613000000001", "34.16984 -118.38582000000001", "34.1696 -118.38555000000001", "34.16937 -118.38533000000001", "34.169230000000006 -118.38520000000001", "34.169050000000006 -118.38504", "34.168890000000005 -118.38491", "34.168710000000004 -118.38476000000001", "34.16864 -118.38470000000001", "34.168580000000006 -118.38465000000001", "34.16843 -118.38454000000002", "34.168200000000006 -118.38438000000001", "34.168 -118.38427000000001", "34.16783 -118.38416000000001", "34.16765 -118.38406", "34.16742 -118.38394000000001", "34.167320000000004 -118.38389000000001", "34.16722 -118.38384", "34.167 -118.38374", "34.166760000000004 -118.38364000000001", "34.166410000000006 -118.38349000000001", "34.1662 -118.38340000000001", "34.165440000000004 -118.38306000000001", "34.165150000000004 -118.38294", "34.1651 -118.38292000000001", "34.164860000000004 -118.38281", "34.164590000000004 -118.38269000000001", "34.164320000000004 -118.38257000000002", "34.16375 -118.38232", "34.16366 -118.38228000000001", "34.16302 -118.382", "34.162490000000005 -118.38177", "34.162310000000005 -118.38168", "34.16198 -118.38154000000002", "34.16156 -118.38136000000002", "34.161260000000006 -118.38123000000002", "34.16066 -118.38096000000002", "34.16028 -118.38080000000001", "34.16028 -118.38080000000001", "34.16022 -118.38081000000001", "34.16017 -118.38082000000001", "34.16013 -118.38082000000001", "34.160090000000004 -118.38082000000001", "34.160050000000005 -118.38081000000001", "34.15997 -118.38078000000002", "34.15984 -118.38073000000001", "34.15977 -118.3807", "34.15959 -118.38064000000001", "34.15935 -118.38056", "34.15921 -118.38051000000002", "34.159060000000004 -118.38046000000001", "34.15885 -118.38040000000001", "34.158660000000005 -118.38035", "34.15863 -118.38034", "34.158480000000004 -118.38029000000002", "34.158170000000005 -118.38018000000001", "34.15814 -118.38018000000001", "34.15811 -118.38017", "34.15802 -118.38015000000001", "34.157900000000005 -118.38014000000001", "34.1578 -118.38013000000001", "34.15771 -118.38014000000001", "34.15766 -118.38015000000001", "34.15766 -118.38015000000001", "34.15766 -118.38012", "34.15766 -118.37977000000001", "34.15767 -118.37953", "34.15766 -118.37924000000001", "34.157650000000004 -118.37904", "34.157650000000004 -118.37904", "34.15748 -118.37904", "34.157410000000006 -118.37904", "34.157320000000006 -118.37907000000001", "34.15704 -118.37919000000001", "34.15691 -118.37925000000001", "34.15675 -118.37932", "34.156710000000004 -118.37934000000001", "34.15663 -118.37937000000001", "34.156490000000005 -118.3794", "34.15644 -118.37941000000001", "34.15639 -118.37941000000001", "34.15635 -118.37941000000001", "34.156310000000005 -118.37941000000001", "34.15627 -118.37941000000001", "34.15621 -118.3794", "34.15614 -118.37938000000001", "34.1561 -118.37936", "34.15605 -118.37935000000002", "34.156020000000005 -118.37933000000001", "34.15598 -118.37931", "34.15589 -118.37927", "34.15578 -118.37921000000001", "34.155680000000004 -118.37916000000001", "34.155530000000006 -118.37909", "34.15545 -118.37906000000001", "34.1554 -118.37904", "34.155350000000006 -118.37903000000001", "34.155300000000004 -118.37901000000001", "34.15525 -118.379", "34.1552 -118.379", "34.155150000000006 -118.37899000000002", "34.154900000000005 -118.37898000000001", "34.154900000000005 -118.37898000000001", "34.154900000000005 -118.37915000000001", "34.154900000000005 -118.37927", "34.15489 -118.37937000000001", "34.154880000000006 -118.37946000000001", "34.15487 -118.37957000000002", "34.15484 -118.37981", "34.15482 -118.3799", "34.1548 -118.38005000000001", "34.15478 -118.38014000000001", "34.154770000000006 -118.38025", "34.15476 -118.38034", "34.15476 -118.38045000000001", "34.154740000000004 -118.38064000000001", "34.154700000000005 -118.38153000000001", "34.15469 -118.38190000000002", "34.15467 -118.38214", "34.15467 -118.38216000000001", "34.15466 -118.38219000000001", "34.154650000000004 -118.38223", "34.154590000000006 -118.38234000000001", "34.15458 -118.38307", "34.15458 -118.38387000000002", "34.15458 -118.38401", "34.154560000000004 -118.3841", "34.15455 -118.38753000000001", "34.15455 -118.38774000000001", "34.15455 -118.38794000000001", "34.154540000000004 -118.39151000000001", "34.154540000000004 -118.39167", "34.154540000000004 -118.39193000000002", "34.154540000000004 -118.39218000000001", "34.154540000000004 -118.39227000000001", "34.154540000000004 -118.39279", "34.15455 -118.39295000000001", "34.154540000000004 -118.39322000000001", "34.154540000000004 -118.39345000000002", "34.15453 -118.39367000000001", "34.15453 -118.39439000000002", "34.154520000000005 -118.39529", "34.154520000000005 -118.39631000000001", "34.154520000000005 -118.39649000000001", "34.154520000000005 -118.39667000000001", "34.154520000000005 -118.39699000000002", "34.15453 -118.39719000000001", "34.154540000000004 -118.39735", "34.15455 -118.39746000000001", "34.154560000000004 -118.39758", "34.15457 -118.39775000000002", "34.154590000000006 -118.39792000000001", "34.154630000000004 -118.39814000000001", "34.15466 -118.3983", "34.15469 -118.39848", "34.15473 -118.39865", "34.15475 -118.39874", "34.154770000000006 -118.39882000000001", "34.15482 -118.39897", "34.154900000000005 -118.39924", "34.155 -118.39955", "34.155120000000004 -118.39984000000001", "34.15525 -118.40012000000002", "34.15536 -118.40032000000001", "34.155860000000004 -118.40131000000001", "34.155930000000005 -118.40146000000001", "34.156000000000006 -118.40160000000002", "34.15608 -118.40177000000001", "34.156150000000004 -118.40192", "34.156220000000005 -118.40209000000002", "34.15635 -118.40241", "34.156400000000005 -118.40257000000001", "34.15645 -118.40274000000001", "34.1565 -118.40289000000001", "34.15654 -118.40306000000001", "34.156580000000005 -118.40323000000001", "34.156620000000004 -118.4034", "34.15668 -118.40373000000001", "34.156710000000004 -118.40389", "34.15672 -118.40397000000002", "34.15673 -118.40406000000002", "34.15675 -118.40424000000002", "34.156760000000006 -118.40439", "34.15677 -118.40453000000001", "34.156780000000005 -118.4047", "34.156780000000005 -118.40487000000002", "34.15679 -118.40504000000001", "34.15679 -118.40522000000001", "34.15679 -118.40528", "34.15679 -118.40552000000001", "34.15679 -118.40604", "34.15679 -118.40688000000002", "34.15681 -118.40987000000001", "34.15681 -118.41088", "34.15681 -118.41244", "34.15682 -118.41315000000002", "34.15682 -118.41351000000002", "34.15683 -118.41378", "34.15683 -118.41379", "34.15683 -118.41397", "34.15684 -118.41644000000001", "34.15684 -118.41735000000001", "34.15684 -118.418", "34.15684 -118.41805000000001", "34.15684 -118.41826", "34.156850000000006 -118.41922000000001", "34.156850000000006 -118.42031000000001", "34.15686 -118.42087000000001", "34.156850000000006 -118.42122", "34.15684 -118.42139000000002", "34.15683 -118.42150000000001", "34.15682 -118.42169000000001", "34.15679 -118.42202", "34.15677 -118.42221", "34.15673 -118.42251", "34.15672 -118.42257000000001", "34.15668 -118.42284000000001", "34.15664 -118.42302000000001", "34.156580000000005 -118.42334000000001", "34.1565 -118.42368", "34.156040000000004 -118.42574", "34.15596 -118.42608000000001", "34.15589 -118.42639000000001", "34.155840000000005 -118.42669000000001", "34.1558 -118.42702000000001", "34.15576 -118.42737000000001", "34.155730000000005 -118.42763000000001", "34.15572 -118.42787000000001", "34.155710000000006 -118.42801000000001", "34.155710000000006 -118.42877000000001", "34.155710000000006 -118.42945", "34.15572 -118.43090000000001", "34.15572 -118.43122000000001", "34.15572 -118.43123000000001", "34.15572 -118.43130000000001", "34.15572 -118.4317", "34.155730000000005 -118.43430000000001", "34.15574 -118.43578000000001", "34.15574 -118.43699000000001", "34.155750000000005 -118.43875000000001", "34.155750000000005 -118.43895", "34.15574 -118.43922", "34.155710000000006 -118.43951000000001", "34.1557 -118.43964000000001", "34.155680000000004 -118.43983000000001", "34.155660000000005 -118.43999000000001", "34.1556 -118.44043", "34.15552 -118.44091000000002", "34.155370000000005 -118.44176000000002", "34.15534 -118.44202000000001", "34.15531 -118.44223000000001", "34.155300000000004 -118.44244", "34.15529 -118.44268000000001", "34.155280000000005 -118.44292000000002", "34.155280000000005 -118.44311", "34.15529 -118.44327000000001", "34.15529 -118.44343", "34.15531 -118.44368000000001", "34.15534 -118.44390000000001", "34.155390000000004 -118.44420000000001", "34.155440000000006 -118.44453000000001", "34.15551 -118.44482", "34.155550000000005 -118.44498000000002", "34.15567 -118.44537000000001", "34.155770000000004 -118.44566", "34.15588 -118.44592000000002", "34.15594 -118.44604000000001", "34.156000000000006 -118.44618000000001", "34.15616 -118.44655000000002", "34.156380000000006 -118.44702000000001", "34.156560000000006 -118.44740000000002", "34.156760000000006 -118.44785000000002", "34.15688 -118.44813", "34.15699 -118.44842000000001", "34.157090000000004 -118.44870000000002", "34.1571 -118.44873000000001", "34.157180000000004 -118.44900000000001", "34.15722 -118.44913000000001", "34.1573 -118.44943", "34.15739 -118.44976000000001", "34.15746 -118.45005", "34.157520000000005 -118.45037", "34.157560000000004 -118.45054", "34.157630000000005 -118.45092000000001", "34.15767 -118.45124000000001", "34.15771 -118.45164000000001", "34.15778 -118.45254000000001", "34.15782 -118.45285000000001", "34.15786 -118.45322000000002", "34.157880000000006 -118.45355", "34.15791 -118.45412", "34.15794 -118.4544", "34.15798 -118.45473000000001", "34.15802 -118.45503000000001", "34.15807 -118.45534", "34.15813 -118.45559000000002", "34.15816 -118.45573", "34.15822 -118.45596", "34.158300000000004 -118.45626000000001", "34.158480000000004 -118.45684000000001", "34.158730000000006 -118.45761000000002", "34.159040000000005 -118.45858000000001", "34.159130000000005 -118.45887", "34.159240000000004 -118.45930000000001", "34.15927 -118.45940000000002", "34.15934 -118.45973000000001", "34.159380000000006 -118.45995", "34.15941 -118.46009000000001", "34.15945 -118.46037000000001", "34.159490000000005 -118.46066", "34.15952 -118.46102", "34.15955 -118.46134", "34.159560000000006 -118.46174", "34.15954 -118.46307000000002", "34.159530000000004 -118.46350000000001", "34.159510000000004 -118.46373000000001", "34.1595 -118.46418000000001", "34.1595 -118.46445000000001", "34.1595 -118.46463000000001", "34.159510000000004 -118.46479000000001", "34.159510000000004 -118.46483", "34.159510000000004 -118.46494000000001", "34.15952 -118.46498000000001", "34.15952 -118.46511000000001", "34.159530000000004 -118.46515000000001", "34.15954 -118.46528", "34.15954 -118.46530000000001", "34.15955 -118.46542000000001", "34.15955 -118.46544000000002", "34.15955 -118.46547000000001", "34.15957 -118.46558", "34.15957 -118.46561000000001", "34.15959 -118.46574000000001", "34.159600000000005 -118.46579000000001", "34.15961 -118.46589000000002", "34.15963 -118.46598000000002", "34.159650000000006 -118.46607000000002", "34.15966 -118.46613", "34.159670000000006 -118.46622", "34.159690000000005 -118.46629000000001", "34.159710000000004 -118.46637000000001", "34.15972 -118.46642000000001", "34.159760000000006 -118.46661", "34.15977 -118.46664000000001", "34.159800000000004 -118.46676000000001", "34.15981 -118.46679", "34.15984 -118.46691000000001", "34.159850000000006 -118.46695000000001", "34.15988 -118.46706", "34.159890000000004 -118.46710000000002", "34.15993 -118.46722000000001", "34.159940000000006 -118.46727000000001", "34.15999 -118.46742", "34.16001 -118.46746", "34.16004 -118.46757000000001", "34.16006 -118.46763000000001", "34.160090000000004 -118.46771000000001", "34.16011 -118.46774", "34.160140000000006 -118.46784000000001", "34.1602 -118.46799000000001", "34.160270000000004 -118.46814", "34.16033 -118.46828000000001", "34.160360000000004 -118.46836", "34.160450000000004 -118.46854", "34.16046 -118.46856000000001", "34.160520000000005 -118.46868", "34.160590000000006 -118.46881", "34.160610000000005 -118.46884000000001", "34.16066 -118.46895", "34.16068 -118.46897000000001", "34.160740000000004 -118.46908", "34.16076 -118.46912", "34.1608 -118.46919000000001", "34.16082 -118.46923000000001", "34.160880000000006 -118.46933000000001", "34.160900000000005 -118.46936000000001", "34.16096 -118.46946000000001", "34.16098 -118.46948", "34.16105 -118.46958000000001", "34.161060000000006 -118.46960000000001", "34.16111 -118.46967000000001", "34.16114 -118.46971", "34.161210000000004 -118.46981000000001", "34.16123 -118.46985000000001", "34.16131 -118.46994000000001", "34.1614 -118.47005000000001", "34.16142 -118.47008000000001", "34.16143 -118.47010000000002", "34.16149 -118.47017000000001", "34.16151 -118.47019000000002", "34.161590000000004 -118.47028000000002", "34.16161 -118.47030000000001", "34.161680000000004 -118.47038", "34.16171 -118.47041000000002", "34.161770000000004 -118.47048000000001", "34.161880000000004 -118.47059000000002", "34.1619 -118.47062000000001", "34.162000000000006 -118.47072000000001", "34.16208 -118.47079000000001", "34.1621 -118.47081000000001", "34.16218 -118.47089000000001", "34.16228 -118.47098000000001", "34.1623 -118.471", "34.16252 -118.47118", "34.16274 -118.47136", "34.16317 -118.47172", "34.16326 -118.47179000000001", "34.16339 -118.47189000000002", "34.163500000000006 -118.47198000000002", "34.163590000000006 -118.47205000000001", "34.163610000000006 -118.47207000000002", "34.16371 -118.47216000000002", "34.16382 -118.47227000000001", "34.163900000000005 -118.47235", "34.163990000000005 -118.47244", "34.164010000000005 -118.47247000000002", "34.164080000000006 -118.47255000000001", "34.16418 -118.47266", "34.1642 -118.47269000000001", "34.16427 -118.47278000000001", "34.16434 -118.47288", "34.164440000000006 -118.47301000000002", "34.16452 -118.47314000000001", "34.16467 -118.47340000000001", "34.164820000000006 -118.47368000000002", "34.164840000000005 -118.47373", "34.16489 -118.47385000000001", "34.164950000000005 -118.47399000000001", "34.16499 -118.47409", "34.16499 -118.47411000000001", "34.165000000000006 -118.47412000000001", "34.16503 -118.47428000000001", "34.16507 -118.4744", "34.165110000000006 -118.47455000000001", "34.16512 -118.47458", "34.16516 -118.47470000000001", "34.16517 -118.47474000000001", "34.165200000000006 -118.47484000000001", "34.16521 -118.47488000000001", "34.165240000000004 -118.47499", "34.16525 -118.47503", "34.16528 -118.47518000000001", "34.165310000000005 -118.47531000000001", "34.16532 -118.47537000000001", "34.16534 -118.47548", "34.16537 -118.47564000000001", "34.16539 -118.47578000000001", "34.165400000000005 -118.47584", "34.16541 -118.47592000000002", "34.165420000000005 -118.47596000000001", "34.16543 -118.47607", "34.16543 -118.47612000000001", "34.16546 -118.47649000000001", "34.165470000000006 -118.47673", "34.165470000000006 -118.47688000000001", "34.165470000000006 -118.47703000000001", "34.165470000000006 -118.47734000000001", "34.165470000000006 -118.4775", "34.16539 -118.48362000000002", "34.165350000000004 -118.48638000000001", "34.165310000000005 -118.48956000000001", "34.1653 -118.48975000000002", "34.165290000000006 -118.48987000000001", "34.165290000000006 -118.48998", "34.165290000000006 -118.49010000000001", "34.165290000000006 -118.49021", "34.16528 -118.49034", "34.165290000000006 -118.49046000000001", "34.165290000000006 -118.49059000000001", "34.165290000000006 -118.49081000000001", "34.1653 -118.49093", "34.165330000000004 -118.49129", "34.165380000000006 -118.49167000000001", "34.16545 -118.49206000000001", "34.16552 -118.49237000000001", "34.16554 -118.49244000000002", "34.165670000000006 -118.49287000000001", "34.16575 -118.49309000000001", "34.16584 -118.49332000000001", "34.16601 -118.4937", "34.166180000000004 -118.49402", "34.166470000000004 -118.49451", "34.167860000000005 -118.49667000000001", "34.16805 -118.49696000000002", "34.168150000000004 -118.4971", "34.168200000000006 -118.49717000000001", "34.16846 -118.49757000000001", "34.16868 -118.49792000000001", "34.16892 -118.49828000000001", "34.16913 -118.49861000000001", "34.169180000000004 -118.49869000000001", "34.169450000000005 -118.49910000000001", "34.169650000000004 -118.49941000000001", "34.16977 -118.49960000000002", "34.16993 -118.49986000000001", "34.17009 -118.50015", "34.170190000000005 -118.50033", "34.17033 -118.5006", "34.17038 -118.50072000000002", "34.17047 -118.50093000000001", "34.17054 -118.50110000000001", "34.170550000000006 -118.50111000000001", "34.17065 -118.50138000000001", "34.170700000000004 -118.50151000000001", "34.17074 -118.50163", "34.17087 -118.50199", "34.170950000000005 -118.50231000000001", "34.17103 -118.50265", "34.17109 -118.50294000000001", "34.171150000000004 -118.50329", "34.17118 -118.50347000000001", "34.171200000000006 -118.50367000000001", "34.171220000000005 -118.50379000000001", "34.17123 -118.50395", "34.171240000000004 -118.50407000000001", "34.171260000000004 -118.50438000000001", "34.17127 -118.50458", "34.17127 -118.50493000000002", "34.17127 -118.50543", "34.17128 -118.50655", "34.17128 -118.50832000000001", "34.17128 -118.5091", "34.17128 -118.50975000000001", "34.17128 -118.50982", "34.17128 -118.51001000000001", "34.17128 -118.51050000000001", "34.17128 -118.51195000000001", "34.17128 -118.51207000000001", "34.17128 -118.51237", "34.17128 -118.51272000000002", "34.17128 -118.51302000000001", "34.17128 -118.51326000000002", "34.17128 -118.51361000000001", "34.17128 -118.51420000000002", "34.17128 -118.51431000000001", "34.17128 -118.51433000000002", "34.17128 -118.51537", "34.17127 -118.51565000000001", "34.17128 -118.51656000000001", "34.17128 -118.51771000000001", "34.17128 -118.51908000000002", "34.17128 -118.52025", "34.17128 -118.52142", "34.17127 -118.52181000000002", "34.17128 -118.52545", "34.17128 -118.52669000000002", "34.17128 -118.52794000000002", "34.17128 -118.52831", "34.171290000000006 -118.52860000000001", "34.1713 -118.52890000000001", "34.17132 -118.52918000000001", "34.17137 -118.52956", "34.17141 -118.52982000000002", "34.171440000000004 -118.53003000000001", "34.171490000000006 -118.53025000000001", "34.17155 -118.53054000000002", "34.17161 -118.53078000000001", "34.1717 -118.53108", "34.171800000000005 -118.53139000000002", "34.171910000000004 -118.53170000000001", "34.172000000000004 -118.53191000000001", "34.172160000000005 -118.5323", "34.17233 -118.5327", "34.17239 -118.53286000000001", "34.17257 -118.53328", "34.172850000000004 -118.53395", "34.17296 -118.53425000000001", "34.17306 -118.53458", "34.17315 -118.53492000000001", "34.173230000000004 -118.53526000000001", "34.17327 -118.53549000000001", "34.173300000000005 -118.5357", "34.17334 -118.53602000000001", "34.17336 -118.53630000000001", "34.173370000000006 -118.53654000000002", "34.173390000000005 -118.53806000000002", "34.1734 -118.53829", "34.173410000000004 -118.53849000000001", "34.17342 -118.53893000000001", "34.17344 -118.53956000000001", "34.17344 -118.54050000000001", "34.17344 -118.54063000000001", "34.17344 -118.54075", "34.17345 -118.54079000000002", "34.17345 -118.54094", "34.17351 -118.54472000000001", "34.17351 -118.54473000000002", "34.17353 -118.54611000000001", "34.17356 -118.54754000000001", "34.173590000000004 -118.55015000000002", "34.173610000000004 -118.55083", "34.173610000000004 -118.55108000000001", "34.17362 -118.55122000000001", "34.17362 -118.55225000000002", "34.173640000000006 -118.55346000000002", "34.173640000000006 -118.55347", "34.17367 -118.55552000000002", "34.173680000000004 -118.55583000000001", "34.173680000000004 -118.55592000000001", "34.17369 -118.55599000000001", "34.173700000000004 -118.55607", "34.173700000000004 -118.55630000000001", "34.173700000000004 -118.55654000000001", "34.173700000000004 -118.55698000000001", "34.17372 -118.55785000000002", "34.173730000000006 -118.55831", "34.173730000000006 -118.55870000000002", "34.173730000000006 -118.55881000000001", "34.173730000000006 -118.55913000000001", "34.173730000000006 -118.55938", "34.17372 -118.55953000000001", "34.17372 -118.55969", "34.17371 -118.55982000000002", "34.173700000000004 -118.55996", "34.173680000000004 -118.56031000000002", "34.173640000000006 -118.56078000000001", "34.17363 -118.561", "34.17356 -118.56174000000001", "34.17354 -118.56196000000001", "34.173480000000005 -118.56267000000001", "34.173190000000005 -118.56606000000001", "34.173100000000005 -118.56709000000001", "34.17305 -118.56747000000001", "34.173030000000004 -118.56763000000001", "34.17296 -118.56819000000002", "34.17291 -118.56849000000001", "34.17289 -118.56859000000001", "34.172850000000004 -118.56883", "34.172810000000005 -118.56902000000001", "34.172790000000006 -118.56911000000001", "34.17273 -118.56938000000001", "34.172670000000004 -118.56966000000001", "34.17257 -118.57007000000002", "34.17246 -118.57046000000001", "34.17235 -118.57084", "34.172320000000006 -118.57092000000002", "34.17224 -118.57117000000001", "34.17215 -118.57145000000001", "34.17199 -118.57188000000001", "34.17159 -118.57297000000001", "34.171290000000006 -118.57377000000001", "34.17114 -118.57416", "34.17099 -118.57454000000001", "34.170700000000004 -118.57533000000001", "34.17063 -118.5755", "34.170550000000006 -118.57572", "34.17038 -118.57616000000002", "34.17013 -118.57683000000002", "34.16975 -118.57784000000001", "34.1694 -118.57876", "34.169250000000005 -118.57916000000002", "34.16913 -118.57950000000001", "34.169070000000005 -118.57965000000002", "34.16901 -118.57982000000001", "34.16888 -118.58023000000001", "34.16874 -118.58068000000002", "34.168620000000004 -118.58113000000002", "34.168530000000004 -118.58153000000001", "34.168420000000005 -118.58201000000001", "34.168350000000004 -118.58236000000001", "34.16828 -118.58278000000001", "34.168220000000005 -118.58315", "34.16817 -118.58353000000001", "34.168150000000004 -118.58372000000001", "34.1681 -118.58413000000002", "34.16807 -118.58454", "34.16805 -118.58486", "34.16803 -118.58527000000001", "34.168020000000006 -118.5857", "34.168020000000006 -118.58632000000001", "34.168020000000006 -118.58654000000001", "34.168040000000005 -118.58705", "34.16809 -118.58773000000001", "34.168110000000006 -118.58792000000001", "34.168130000000005 -118.58815000000001", "34.16816 -118.58838000000002", "34.168200000000006 -118.5887", "34.16823 -118.58892000000002", "34.168290000000006 -118.58934", "34.16839 -118.58995000000002", "34.168600000000005 -118.59132000000001", "34.16872 -118.59214000000001", "34.16903 -118.59413", "34.16903 -118.59413", "34.169140000000006 -118.5943", "34.169160000000005 -118.59433000000001", "34.169160000000005 -118.59437000000001", "34.16917 -118.59439", "34.169180000000004 -118.59446000000001", "34.169230000000006 -118.5948", "34.169250000000005 -118.59493", "34.169270000000004 -118.59503000000001", "34.1693 -118.59514000000001", "34.16933 -118.59531000000001", "34.16942 -118.59564", "34.169470000000004 -118.59587", "34.169520000000006 -118.59606000000001", "34.16959 -118.59641", "34.169610000000006 -118.59648000000001", "34.169630000000005 -118.59656000000001", "34.169650000000004 -118.59662000000002", "34.16969 -118.59675000000001", "34.16969 -118.59676", "34.1698 -118.59721", "34.16986 -118.59745000000001", "34.16986 -118.59745000000001", "34.17049 -118.59745000000001", "34.17092 -118.59745000000001", "34.17139 -118.59745000000001", "34.171490000000006 -118.59745000000001", "34.17231 -118.59746000000001", "34.17311 -118.59746000000001", "34.17331 -118.59739", "34.174640000000004 -118.59739", "34.17515 -118.59739", "34.17521 -118.59739", "34.17613 -118.59739", "34.176640000000006 -118.59739", "34.177240000000005 -118.59739", "34.178380000000004 -118.59739", "34.178490000000004 -118.59739", "34.17868 -118.59740000000001", "34.1792 -118.59740000000001", "34.17926 -118.59740000000001", "34.17931 -118.59740000000001", "34.180240000000005 -118.59739", "34.18032 -118.59740000000001", "34.18048 -118.59740000000001", "34.18094 -118.59739", "34.180980000000005 -118.59739", "34.18202 -118.59740000000001", "34.18215 -118.59740000000001", "34.182860000000005 -118.59740000000001", "34.18372 -118.59740000000001", "34.18388 -118.59740000000001", "34.1843 -118.59740000000001", "34.18457 -118.59740000000001", "34.18488 -118.59740000000001", "34.185680000000005 -118.59740000000001", "34.18598 -118.59741000000001", "34.186350000000004 -118.59742000000001", "34.18685 -118.59740000000001", "34.187000000000005 -118.59741000000001", "34.187200000000004 -118.59741000000001", "34.187340000000006 -118.59741000000001", "34.1875 -118.59741000000001", "34.18769 -118.59740000000001", "34.188370000000006 -118.59740000000001", "34.18858 -118.59740000000001", "34.1886 -118.59740000000001", "34.188610000000004 -118.59741000000001", "34.18863 -118.59742000000001", "34.188700000000004 -118.59747000000002", "34.189 -118.59747000000002", "34.18907 -118.59748", "34.189170000000004 -118.59748", "34.189550000000004 -118.59747000000002", "34.18967 -118.59747000000002", "34.1903 -118.59747000000002", "34.19037 -118.59747000000002", "34.19052 -118.59747000000002", "34.190920000000006 -118.59748", "34.19099 -118.59747000000002", "34.19109 -118.59747000000002", "34.191300000000005 -118.59747000000002", "34.191900000000004 -118.59748", "34.192640000000004 -118.59748", "34.192710000000005 -118.59748", "34.19277 -118.59748", "34.19305 -118.59748", "34.19332 -118.59748", "34.193780000000004 -118.59748", "34.19437 -118.59749000000001", "34.194950000000006 -118.59750000000001", "34.195350000000005 -118.59750000000001", "34.19538 -118.59750000000001", "34.19541 -118.59750000000001", "34.19548 -118.59750000000001", "34.195600000000006 -118.59750000000001", "34.195930000000004 -118.59750000000001", "34.196180000000005 -118.59750000000001", "34.19643 -118.59750000000001", "34.1965 -118.59750000000001", "34.196540000000006 -118.59750000000001", "34.196580000000004 -118.59750000000001", "34.19664 -118.59751000000001", "34.196650000000005 -118.59751000000001", "34.19668 -118.59752", "34.196740000000005 -118.59753", "34.19679 -118.59755000000001", "34.19682 -118.59756000000002", "34.19702 -118.59762", "34.197190000000006 -118.59767000000001", "34.197410000000005 -118.59773000000001", "34.197520000000004 -118.59774000000002", "34.197590000000005 -118.59775", "34.197630000000004 -118.59775", "34.197950000000006 -118.59775", "34.19894 -118.59773000000001", "34.199220000000004 -118.59772000000001", "34.19971 -118.59772000000001", "34.199850000000005 -118.59772000000001", "34.200100000000006 -118.59772000000001", "34.20049 -118.59772000000001", "34.20103 -118.59772000000001", "34.20158 -118.59773000000001", "34.201890000000006 -118.59773000000001", "34.20243 -118.59773000000001", "34.20262 -118.59773000000001", "34.2027 -118.59773000000001", "34.20286 -118.59771", "34.203030000000005 -118.59767000000001", "34.20326 -118.59760000000001", "34.2034 -118.59756000000002", "34.203520000000005 -118.59754000000001", "34.203540000000004 -118.59753", "34.2036 -118.59752", "34.20367 -118.59752", "34.20373 -118.59752", "34.20378 -118.59752", "34.20396 -118.59752", "34.20413 -118.59752", "34.20468 -118.59752", "34.20514 -118.59752", "34.20599 -118.59752", "34.206500000000005 -118.59752", "34.207440000000005 -118.59752", "34.2083 -118.59751000000001", "34.208740000000006 -118.59751000000001", "34.20935 -118.59752", "34.21011 -118.59752"]'

tester = all_scores.get_all_scores(test,"pickle_test.p",0.007)
print(tester)
#grid_obj = Grid(pickle_file_name = "pickle_test.p")
#print(grid_obj.max_score)
