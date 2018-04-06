from process_1.apa_login import Apa_login
# from process_2.apa_processmap import Show_processmap
# from Addcompany import test_addprocess_apa
import unittest,HTMLTestRunner,multiprocessing,sys,os,time
import process_1.apa_login
# import process_2.apa_processmap
sys.path.append('C:/Users/huanri/Documents/apa_auto/test_case')



class Apa_test_suite(unittest.TestSuite):
	@staticmethod
	# def suite():
	# 	suite = unittest.TestSuite()
	# 	# suite = unittest.TestLoader().loadTestsFromTestCase(Show_processmap)
	# 	# suite = unittest.TestLoader().loadTestsFromTestCase(Apa_login)
	# 	suite.addTest(unittest.makeSuite(Apa_login))
	# 	# suite.addTest(unittest.makeSuite(Show_processmap))
	# 	# suite.addTest(unittest.makeSuite(Addcompany))
	# 	return suite
	# 	# self.run(suite)

	def createsuite():
		processdir = []
		list_proc = os.listdir('C:/Users/huanri/Documents/apa_auto/test_case')

		for folders in list_proc:
			if "process" in folders:
				processdir.append(folders)		
		# print processdir
		suite = []
		for n in processdir:
			testunit = unittest.TestSuite()
			discover =  unittest.defaultTestLoader.discover(str(n), pattern = 'apa_*.py',top_level_dir = r'C:/Users/huanri/Documents/apa_auto')
			# print discover
			for test_suite in discover:
				# testunit.addTest(unittest.makeSuite(test_suite))
				for  test_case in test_suite:
					testunit.addTest(test_case)			
					suite.append(testunit)
		print suite
		return suite,processdir
	@staticmethod
	def runcase(suite,processdir):
		processlist = []
		# now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
		# test_result = 'C:/Users/huanri/Documents/apa_auto/test_report/' + now +'_test_result.html'
		test_result = 'C:/Users/huanri/Documents/apa_auto/test_report/apa_testreport.html'
		fp = file(test_result, 'w')
		for i in suite:
			runner = unittest.TextTestRunner()
			t = 0
			runner = HTMLTestRunner.HTMLTestRunner(
			stream = fp,
			title = u'APA_Test_Report',
			description = u'Test Case Excution Report'
			)
			proc = multiprocessing.Process(target = runner.run, args = (i,))
			# print proc
			processlist.append(proc)
			# t = t+1
			# print processlist
		for i in processlist:
			i.start()
		for i in processlist:
			i.join() 
		# fp.close()

if __name__ == '__main__':
	suite = Apa_test_suite.createsuite()
	Apa_test_suite.runcase(suite[0],suite[1])
	

