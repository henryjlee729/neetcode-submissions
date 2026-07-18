class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = []
        for i in range(0, numCourses):
            courses.append([])
        for (course, prerequisite) in prerequisites:
            courses[prerequisite].append(course)

        visiting = set()
        completed = set()
        for course in range(0, numCourses):
            if not self.dfs(course, visiting, completed, courses):
                return False

        return True

    def dfs(self, course, visiting, completed, courses):
        if course in visiting:
            return False
        if course in completed:
            return True 

        visiting.add(course)
        for nextCourse in courses[course]:
            if not self.dfs(nextCourse, visiting, completed, courses):
                return False
           
        visiting.remove(course)
        completed.add(course)
        return True